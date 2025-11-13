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
GET /v1/dashboard/
Descripción: Devuelve el progreso y la rutina asociada a un usuario.

Parámetros (query):

user_name (string, requerido)

Ejemplo de llamada: GET https://videojuego-backend-3kce.onrender.com/v1/dashboard/?user_name=Ornella

Respuesta:

json
{
  "user_name": "Ornella",
  "progress": 75,
  "routine": { "id": 2, "name": "Rutina Avanzada", "duration": 30 }
}
GET /v1/oracle/
Descripción: Devuelve un consejo o mensaje motivacional aleatorio.

Ejemplo de llamada: GET https://videojuego-backend-3kce.onrender.com/v1/oracle/

Respuesta:

json
{ "message": "Recuerda que cada paso cuenta hacia tu meta." }
POST /v1/routines/
Descripción: Crea una nueva rutina.

Body (JSON):

json
{ "name": "Rutina Personalizada", "duration": 20 }
Ejemplo de llamada: POST https://videojuego-backend-3kce.onrender.com/v1/routines/ Content-Type: application/json

Respuesta:

json
{ "id": 3, "name": "Rutina Personalizada", "duration": 20 }
Notas para frontend
Ejemplo en React:

javascript
fetch("https://videojuego-backend-3kce.onrender.com/v1/dashboard/?user_name=Ornella")
  .then(res => res.json())
  .then(data => console.log(data));
