# API Contract – Proyecto Videojuego

Base URL: https://videojuego-backend-3kce.onrender.com

---

## General
- Formato de respuesta: JSON
- Autenticación: No requerida (actualmente)
- Versionado: Todos los endpoints están bajo /v1/

---

## Endpoints

### GET /v1/routines/
**Descripción:** Lista todas las rutinas disponibles.

**Ejemplo de llamada:**
GET https://videojuego-backend-3kce.onrender.com/v1/routines/

**Respuesta:**
```json
[
  { "id": 1, "name": "Rutina Básica", "duration": 15 },
  { "id": 2, "name": "Rutina Avanzada", "duration": 30 }
]


