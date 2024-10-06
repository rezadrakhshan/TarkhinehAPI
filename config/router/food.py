from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.schemas import FoodCreate, FoodRemove
from db.models import Food

router = APIRouter(tags=["Food"])


@router.get("/")
def main(db: Session = Depends(get_db)):
    foods = db.query(Food).all()
    return foods


@router.post("/food/create", response_model=FoodCreate)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    try:
        calculate_finall_price = food.price - ((food.price * food.discount) / 100)
        new_food = Food(
            title=food.title,
            description=food.description,
            price=food.price,
            discount=food.discount,
            finall_price=calculate_finall_price,
            image=food.image,
        )
        db.add(new_food)
        db.commit()
        db.refresh(new_food)
        return new_food
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/food/remove")
def remove_food(food: FoodRemove, db: Session = Depends(get_db)):
    try:
        selected_food = db.query(Food).filter(Food.id == food.id).first()
        if selected_food:
            db.delete(selected_food)
            db.commit()
            raise HTTPException(status_code=200,detail="Food was deleted")
        else:
            raise HTTPException(status_code=404, detail="Food not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
