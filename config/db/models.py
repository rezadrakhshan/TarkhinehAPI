from .database import Base
from sqlalchemy.types import String, Integer, Float
from sqlalchemy import Column


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    discount = Column(Integer)
    finall_price = Column(Float)
    image = Column(String)
