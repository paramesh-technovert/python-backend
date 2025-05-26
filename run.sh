#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

# Automatically install requirements recommended only for local use 
pip install -r requirements.txt 

# Activate virtual environment (Windows path)
source .venv/Scripts/activate

# Run FastAPI using Python module to avoid permission issues
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 
