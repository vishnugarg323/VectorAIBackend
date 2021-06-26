from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def ping():
    return {"status" : "VectorAI Backend is UP"}