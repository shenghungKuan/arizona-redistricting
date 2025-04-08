from fastapi import APIRouter

router = APIRouter(
    prefix="/arizona",
)

@router.get("/test")
async def test():
    return {"message": "This is a test"}