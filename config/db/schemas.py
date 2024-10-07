from pydantic import BaseModel
from typing import Optional, List


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


class ProfileResponse(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone: str
    birth_date: str
    username: str
    address: List["AddressResponse"] = []


class UpdateProfile(BaseModel):
    id: int
    firstname: Optional[str] = ""
    lastname: Optional[str] = ""
    email: Optional[str] = ""
    phone: Optional[str] = ""
    birth_date: Optional[str] = ""
    username: Optional[str] = ""


class RemoveProfile(BaseModel):
    id: int


class AddressCreate(BaseModel):
    title: str
    is_your_receiver_delivery: Optional[bool] = False
    phone: str
    address: str
    profile_id: int


class AddressResponse(BaseModel):
    title: str
    is_your_receiver_delivery: Optional[bool] = False
    phone: str
    address: str
    profile_id: int

    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    id: int
    title: Optional[str] = ""
    is_your_receiver_delivery: Optional[bool] = False
    phone: Optional[str] = ""
    address: Optional[str] = ""
    profile_id: Optional[int] = 0

class RemoveAddress(BaseModel):
    id:int