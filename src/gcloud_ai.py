#!/usr/bin/env python3
"""
Optional Google Cloud Vertex AI wrapper.

This module provides a safe, non-blocking integration point for Vertex AI text
generation. It tries to import and call the Google Cloud SDK when available and
when credentials are set via environment variables. On any error it returns
None so the application can gracefully fall back to local logic.
"""
import os
import logging
import json

try:
    from google.cloud import aiplatform
    GCLOUD_AVAILABLE = True
except Exception:
    GCLOUD_AVAILABLE = False


def is_available() -> bool:
    """Return True if the google-cloud-aiplatform package is installed and
    application credentials are present in environment.
    """
    creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    return GCLOUD_AVAILABLE and bool(creds)


def generate_text(
    prompt: str,
    project: str = None,
    location: str = "us-central1",
    model: str = None,
    max_length: int = 256,
):
    """
    Generate text using Vertex AI if possible.

    Returns generated text on success, or None on any failure.

    Notes:
        - To enable: install `google-cloud-aiplatform` and set
            `GOOGLE_APPLICATION_CREDENTIALS` to a service account JSON file.
        - Optionally set `GOOGLE_CLOUD_PROJECT`, `VERTEX_LOCATION`, and
            `VERTEX_MODEL_ID`.
    - This function is intentionally defensive: any import / call errors will
      be caught and logged, and None will be returned so the caller can fall
      back to local behaviour.
    """
    if not GCLOUD_AVAILABLE:
        logging.debug("gcloud_ai: google-cloud-aiplatform not installed")
        return None

    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        logging.debug("gcloud_ai: GOOGLE_APPLICATION_CREDENTIALS not set")
        return None

    try:
        # Prefer explicit parameters or environment values
        proj = project or os.environ.get("GOOGLE_CLOUD_PROJECT")
        loc = location or os.environ.get("VERTEX_LOCATION", "us-central1")
        model_id = model or os.environ.get("VERTEX_MODEL_ID")

        # Initialize client (idempotent)
        aiplatform.init(project=proj, location=loc)

        # If user provided a high-level TextGenerationModel API is available,
        # try it first (newer versions of the SDK expose this helper).
        try:
            TextModel = getattr(aiplatform, "TextGenerationModel", None)
            if TextModel and model_id:
                tg = TextModel.from_pretrained(model_id)
                res = tg.predict(prompt, max_output_tokens=max_length)
                # Response shape may vary by SDK version
                if hasattr(res, "text"):
                    return res.text
                return str(res)
        except Exception:
            # Continue to lower-level client if high-level API not available
            logging.debug(
                "gcloud_ai: high-level TextGenerationModel failed",
                exc_info=True,
            )

        # Use PredictionServiceClient fallback
        client = aiplatform.gapic.PredictionServiceClient()

        # Build model resource name if not provided as full path
        if model_id and model_id.startswith("projects/"):
            name = model_id
        else:
            # If project is missing, rely on aiplatform.init to have set it
            effective_project = proj or aiplatform.init().project
            effective_location = loc
            effective_model = model_id or "text-bison@001"
            name = (
                "projects/" + effective_project
                + "/locations/" + effective_location
                + "/models/" + effective_model
            )

        instances = [{"content": prompt}]
        parameters = {"maxOutputTokens": max_length}

        request = {
            "endpoint": name,
            "instances": instances,
            "parameters": parameters,
        }
        result = client.predict(request=request)

        preds = getattr(result, "predictions", None)
        if preds:
            first = preds[0]
            if isinstance(first, dict):
                # Common keys used by Vertex AI responses
                for key in ("content", "text", "output"):
                    if key in first:
                        return first[key]
                return json.dumps(first)
            return str(first)

        return None
    except Exception:
        logging.exception("gcloud_ai: Vertex AI generation failed")
        return None
