from fastapi import APIRouter

from app.api import crud
from app.api.models.model import CardDB, CardSchema

router = APIRouter()


@router.post("/", response_model=CardDB, status_code=201)
async def create_card(payload: CardSchema):
    card_id = await crud.post(payload)

    response_object = {
        "id": card_id,
        "title": payload.title,
        "type": payload.type,
    }
    return response_object
