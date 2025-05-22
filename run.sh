#!/bin/bash

# Activate virtual environment (Windows path)
source .venv/Scripts/activate

# Run FastAPI using Python module to avoid permission issues
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
