import express from "express";
import axios from "axios";

const app = express();

// Configuration for your deployed Career Advisor application
const url = `https://career-advisor-9gjv.onrender.com/_keepalive`; // Uses your existing keepalive endpoint
const interval = 30000; // 30 seconds

function reloadWebsite() {
  axios
    .get(url)
    .then((response) => {
      console.log(`[${new Date().toISOString()}] Career Advisor website pinged successfully`);
    })
    .catch((error) => {
      console.error(`[${new Date().toISOString()}] Error pinging Career Advisor: ${error.message}`);
    });
}

// Start the ping interval
setInterval(reloadWebsite, interval);

// Basic health endpoint for this service
app.get("/", (req, res) => {
  res.json({ 
    status: "Keep-alive service running",
    target: url,
    interval: `${interval/1000} seconds`,
    service: "Career Advisor Keep-Alive"
  });
});

// Status endpoint to check if the main app is responding
app.get("/status", async (req, res) => {
  try {
    const response = await axios.get(url);
    res.json({
      service: "Career Advisor Keep-Alive",
      target_status: "online",
      target_url: url,
      last_ping: new Date().toISOString()
    });
  } catch (error) {
    res.status(500).json({
      service: "Career Advisor Keep-Alive",
      target_status: "offline",
      target_url: url,
      error: error.message,
      last_ping: new Date().toISOString()
    });
  }
});

const port = 4000;

app.listen(port, () => {
  console.log(`Keep-alive service is running on port ${port}`);
  console.log(`Monitoring Career Advisor at: ${url}`);
  console.log(`Ping interval: ${interval/1000} seconds`);
  console.log(`Service status: http://localhost:${port}`);
  console.log(`Target status check: http://localhost:${port}/status`);
  
  // Start with an immediate ping
  reloadWebsite();
});