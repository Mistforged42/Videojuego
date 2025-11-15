📜 API Contract – Proyecto Videojuego (Actualizado)
Base URL:

Código
https://videojuego-backend-3kce.onrender.com
General
Formato de respuesta: JSON

Autenticación: Header Authorization: Bearer <user_uid>

Versionado: Todos los endpoints bajo /v1/

👤 Perfil de Usuario
GET /v1/profile
Descripción: Obtiene el perfil del usuario autenticado.

Respuesta:

json
{
  "uid": "Mig",
  "email": "mig@example.com",
  "avatar": "url_avatar",
  "xp": 120,
  "level": 3
}
Frontend: Botón “Ver perfil”.

📋 Rutinas
GET /v1/routines/
Descripción: Lista todas las rutinas disponibles.

Respuesta:
```
json
[
  {"id": 1, "title": "Cardio rápido", "duration": "15m"},
  {"id": 2, "title": "Yoga básico", "duration": "20m"}
]
```
Frontend: Pantalla de catálogo con botón “Iniciar rutina”.

POST /v1/routines/
Descripción: Crea una nueva rutina.

Body:

```
json
{"title": "Entrenamiento fuerza", "duration": "30m"}
```
Respuesta:
```
json
{"id": 3, "title": "Entrenamiento fuerza", "duration": "30m"}
```
Frontend: Botón “Crear rutina” con formulario.

POST /v1/routines/{id}/complete?user_uid=<uid>
Descripción: Marca una rutina como completada.

Respuesta:
```
json
{"status": "ok", "routine_id": 1, "user_uid": "Mig"}
```
Frontend: Botón “Completar rutina”.

📈 Progreso
GET /v1/progress/
Descripción: Lista rutinas completadas por el usuario.

Respuesta:
```
json
[
  {"id": 10, "user_uid": "Mig", "routine_id": 1},
  {"id": 11, "user_uid": "Mig", "routine_id": 2}
]
```
Frontend: Pantalla de historial.

📊 Dashboard
GET /v1/dashboard
Descripción: Resumen del usuario + rutinas completadas y disponibles.

Respuesta:
```
json
{
  "user": {"name": "Mig", "level": 3, "xp": 120, "xp_needed": 200},
  "completed_routines": [
    {"id": 1, "title": "Cardio rápido", "duration": "15m"}
  ],
  "available_routines": [
    {"id": 2, "title": "Yoga básico", "duration": "20m"}
  ]
}
```
Frontend: Pantalla principal con progreso y sugerencias.

🔮 Oracle
GET /v1/oracle/
Descripción: Devuelve un consejo motivacional aleatorio.

Respuesta:
```
json
{"message": "Recuerda que cada paso cuenta hacia tu meta."}
```
Frontend: Botón “Consejo del día”.
