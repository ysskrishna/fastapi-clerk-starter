from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core.dbutils import get_db
from models.models import User


security = HTTPBearer()


def parse_clerk_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    pass


def get_current_user(
    payload: dict = Depends(parse_clerk_jwt),
    db: Session = Depends(get_db),
):
    clerk_uid = payload.get("sub")
    user = db.query(User).filter(User.clerk_uid == clerk_uid).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user