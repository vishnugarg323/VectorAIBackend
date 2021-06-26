from app.api.models.model import CardSchema
from app.db import cards, database


async def post(payload: CardSchema):
    query = cards.insert().values(title=payload.title,
                                  type=payload.type, position=payload.position)
    return await database.execute(query=query)


async def get(id: int):
    query = cards.select().where(id == cards.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = cards.select()
    return await database.fetch_all(query=query)


async def change_all_data(id: int, payload: CardSchema):
    query = (
        cards
        .update()
        .where(id == cards.c.id)
        .values(title=payload.title, type=payload.type, position=payload.position)
        .returning(cards.c.id)
    )
    return await database.execute(query=query)


async def change_position(id: int, position: str):
    query = (
        cards
        .update()
        .where(id == cards.c.id)
        .values(position=position)
        .returning(cards.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = cards.delete().where(id == cards.c.id)
    return await database.execute(query=query)
