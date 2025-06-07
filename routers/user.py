from fastapi import APIRouter, Depends, HTTPException
from core.jwtutils import parse_clerk_jwt, get_current_user
from sqlalchemy.orm import Session
from core.dbutils import get_db
from models.models import User
from models.schemas import CreateUserSchema

router = APIRouter()

@router.post("/create")
def create_user(payload:CreateUserSchema, token_payload: dict = Depends(parse_clerk_jwt), db: Session = Depends(get_db)):
    # Check for existing user by clerk_uid
    existing_user = db.query(User).filter(User.clerk_uid == token_payload["sub"]).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists with this Clerk ID")
    
    # Check for existing user by email
    existing_email_user = db.query(User).filter(User.email == payload.email).first()
    if existing_email_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        clerk_uid=token_payload["sub"],
        email=payload.email,
        name=payload.name
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "user_id": new_user.user_id,
        "email": new_user.email
    }

@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "user_id": current_user.user_id,
        "name": current_user.name,
        "email": current_user.email,
        "created_at": current_user.created_at,
        "updated_at": current_user.updated_at
    }