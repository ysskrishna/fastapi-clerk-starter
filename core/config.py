import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    CLERK_JWKS_URL=os.getenv("CLERK_JWKS_URL")
    CLERK_ISSUER=os.getenv("CLERK_ISSUER")