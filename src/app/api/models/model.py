from pydantic import BaseModel


class CardSchema(BaseModel):
    title: str
    type: str


class CardDB(CardSchema):
    id: int
