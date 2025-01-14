from datetime import datetime, timedelta, timezone
import jwt
from typing import Union
import os


class Token():
    def __init__(self):
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.ALGORITHM = "HS256"
        
    def create_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, self.ALGORITHM)
        return encoded_jwt
    
    def decode_token(self, token):
        token = jwt.decode(token, self.SECRET_KEY, self.ALGORITHM)
        decode = token.get("sub")
        return int(decode)