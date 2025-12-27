#!/bin/bash

echo "Start the health test"
curl -sf http://localhost:8001/health
curl -sf http://localhost:8002/health
curl -sf http://localhost:8003/health

echo "Incr test"

echo "Restart Leader"

echo "fault follower down"
