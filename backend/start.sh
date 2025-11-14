#!/usr/bin/env bash
set -e

# Render ya activa .venv por ti. Solo inicia el servidor.
uvicorn app.main:app --host 0.0.0.0 --port 10000
