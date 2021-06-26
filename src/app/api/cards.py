from typing import List
from fastapi import APIRouter

from app.api import crud
from app.api.models.model import CardDB, CardSchema

router = APIRouter()


@router.post("/", response_model=CardDB, status_code=201)
async def create_card(payload: CardSchema):
    card_id = await crud.post(payload)

    response_object = {
        "id": card_id,
        "position": payload.position,
        "title": payload.title,
        "type": payload.type,
    }
    return response_object


@router.get("/", response_model=List[CardDB])
async def get_all_cards():
    return await crud.get_all()


@router.get("/{id}/", response_model=CardDB)
async def get_card(id: int):
    card = await crud.get(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.put("/update-all-data/{id}/", response_model=CardDB)
async def update_all_data(id: int, payload: CardSchema):
    card = await crud.get(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    card_id = await crud.change_all_data(id, payload)

    response_object = {
        "id": card_id,
        "position": payload.position,
        "title": payload.title,
        "type": payload.type,
    }
    return response_object


@router.put("/update-position/{id}/", response_model=CardDB)
async def update_postition(id: int, position: str):
    card = await crud.get(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    card_id = await crud.change_position(id, position)

    response_object = {
        "id": card_id,
        "position": position,
        "title": card.title,
        "type": card.type,
    }
    return response_object


@router.delete("/{id}/", response_model=CardDB)
async def delete_card(id: int):
    card = await crud.get(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    await crud.delete(id)

    return card
