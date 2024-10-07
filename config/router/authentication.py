from fastapi import APIRouter, Depends, HTTPException
from db.schemas import ProfileCreate, AddressCreate
from db.database import get_db
from db.models import Profile, Address
from sqlalchemy.orm import Session

router = APIRouter(tags=["authentication"])


@router.post("/authentication/profile/create/", response_model=ProfileCreate)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    try:
        db_profile = Profile(
            firstname=profile.firstname,
            lastname=profile.lastname,
            email=profile.email,
            phone=profile.phone,
            birth_date=profile.birth_date,
            username=profile.username,
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/authentication/address/create/", response_model=AddressCreate)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    try:
        db_address = Address(
            title=address.title,
            is_your_receiver_delivery=address.is_your_receiver_delivery,
            phone=address.phone,
            address=address.address,
            profile_id=address.profile_id,
        )
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
