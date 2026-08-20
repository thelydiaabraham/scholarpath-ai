from fastapi import APIRouter, Depends
from app.routes.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/me")
def read_own_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }