from pydantic import BaseModel
from typing import Optional


class FoodCreate(BaseModel):
    title: str
    description: str
    price: float
    discount: int
    image: str


class FoodRemove(BaseModel):
    id: int


class ProfileCreate(BaseModel):
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    email: Optional[str] = ""
    phone: str
    birth_date: Optional[str] = ""
    username: Optional[str] = ""


class AddressCreate(BaseModel):
    title: str
    is_your_receiver_delivery: Optional[bool] = False
    phone:str
    address:str
    profile_id:int
