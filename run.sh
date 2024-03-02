#!/bin/bash

# Activate the virtual environment
source ./venv/bin/activate

# Run uvicorn
uvicorn main:app