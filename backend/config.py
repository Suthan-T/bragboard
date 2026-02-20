import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:suthan06@localhost:5432/bragboard"
)