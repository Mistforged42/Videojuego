#!/bin/bash

# Activar entorno virtual
source venv/bin/activate

# Exportar variables de entorno desde .env
export $(grep -v '^#' .env | xargs)

# Levantar servidor FastAPI en host 0.0.0.0 y puerto 10000
uvicorn app.main:app --host 0.0.0.0 --port 10000 --reload
