from app.api.models.model import CardSchema
from app.db import cards, database


async def post(payload: CardSchema):
    query = cards.insert().values(title=payload.title, type=payload.type)
    return await database.execute(query=query)
