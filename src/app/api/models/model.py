from pydantic import BaseModel


class CardSchema(BaseModel):
    title: str
    type: str
    position: int


class CardDB(CardSchema):
    id: int
