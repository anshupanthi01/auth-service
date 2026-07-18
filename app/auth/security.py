from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JoseError
from fastapi import HTTPException