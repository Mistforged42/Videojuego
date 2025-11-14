from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # En modo prueba, tratamos el token como el uid directamente
    payload = {
        "sub": token,
        "email": f"{token}@example.com"
    }
    print("Payload simulado:", payload)
    return payload
