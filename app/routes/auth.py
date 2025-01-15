from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(username: str, password: str):
    # Placeholder authentication logic
    return {"message": "Login successful!"}
