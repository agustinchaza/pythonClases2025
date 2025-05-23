import jwt
from datetime import datetime, timedelta

contrasena = 'mi_contrasena_secreta'
payload = {
    'user_id': 123,
    'contrasena': contrasena,
    'exp': datetime.utcnow() + timedelta(days=1)  # Expira en 1 día
}

# Generar el token

token = jwt.encode(payload, contrasena, algorithm='HS256')
print(f'Token: {token}')




