from pydantic import BaseModel


class FoodCreate(BaseModel):
    title: str
    description: str
    price: float
    discount: int
    image: str


class FoodRemove(BaseModel):
    id: int
