#decode jwt Hs256

import jwt
from datetime import datetime

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsImNvbnRyYXNlbmEiOiJtaV9jb250cmFzZW5hX3NlY3JldGEiLCJleHAiOjE3NDc3ODIzMTB9._AUcv302PvdvEpRekQuwCLA_yYfgl0pf8Te-KryAiBg"

decoded = jwt.decode(token, options={"verify_signature": False})
print(decoded)

