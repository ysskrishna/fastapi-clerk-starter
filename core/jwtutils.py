from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core.dbutils import get_db
from models.models import User
from jwt import PyJWKClient
import jwt
from core.config import Config


security = HTTPBearer()


def parse_clerk_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    try:
        token = credentials.credentials
        audience = None
        jwks_client = PyJWKClient(Config.CLERK_JWKS_URL)
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=audience,
            issuer=Config.CLERK_ISSUER,
        )
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
        )


def get_current_user(
    payload: dict = Depends(parse_clerk_jwt),
    db: Session = Depends(get_db),
):
    clerk_uid = payload.get("sub")
    user = db.query(User).filter(User.clerk_uid == clerk_uid).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user