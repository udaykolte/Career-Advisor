#!/usr/bin/env python3
"""
WSGI entrypoint for servers importing the app as backend.wsgi:app
"""
from backend.app import app, WebCareerAdvisor  # re-export for convenience
