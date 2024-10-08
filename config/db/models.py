from .database import Base
from sqlalchemy.types import String, Integer, Float, Boolean
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    discount = Column(Integer)
    finall_price = Column(Float)
    image = Column(String)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, default="")
    lastname = Column(String, default="")
    email = Column(String, unique=True, default="")
    phone = Column(String, unique=True)
    birth_date = Column(String, default="")
    username = Column(String, default="")
    address = relationship("Address", back_populates="profile")


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    is_your_receiver_delivery = Column(Boolean, default=False)
    phone = Column(String)
    address = Column(String)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    profile = relationship("Profile", back_populates="address")


class Branch(Base):
    __tablename__ = "branchs"
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    address = Column(String)
    phone_number = Column(String)
    working_hours = Column(String)
    image = Column(String)