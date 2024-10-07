from fastapi import APIRouter, Depends, HTTPException
from db.schemas import (
    ProfileCreate,
    AddressCreate,
    ProfileResponse,
    UpdateProfile,
    RemoveProfile,
    UpdateAddress,
    RemoveAddress,
)
from db.database import get_db
from db.models import Profile, Address
from sqlalchemy.orm import Session
from typing import List

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


@router.get("/authentication/profile/", response_model=List[ProfileResponse])
def get_profiles(db: Session = Depends(get_db)):
    db_profile = db.query(Profile).all()
    return db_profile


@router.put("/authentication/profile/update/", response_model=UpdateProfile)
def update_profile(profile: UpdateProfile, db: Session = Depends(get_db)):
    try:
        db_profile = db.query(Profile).filter(Profile.id == profile.id).first()
        if db_profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        db_profile.firstname = (
            profile.firstname if profile.firstname != "" else db_profile.firstname
        )
        db_profile.lastname = (
            profile.lastname if profile.lastname != "" else db_profile.lastname
        )
        db_profile.email = profile.email if profile.email != "" else db_profile.email
        db_profile.phone = profile.phone if profile.phone != "" else db_profile.phone
        db_profile.birth_date = (
            profile.birth_date if profile.birth_date != "" else db_profile.birth_date
        )
        db_profile.username = (
            profile.username if profile.username != "" else db_profile.username
        )
        db.commit()
        db.refresh(db_profile)
        raise HTTPException(status_code=200, detail="Profile updated")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/authentication/profile/delete/", response_model=RemoveProfile)
def remove_profile(profile: RemoveProfile, db: Session = Depends(get_db)):
    try:
        db_profile = db.query(Profile).filter(Profile.id == profile.id).first()
        if db_profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        for i in db_profile.address:
            db_address = db.query(Address).filter(Address.id == i.id).first()
            db.delete(db_address)
            db.commit()
        db.delete(db_profile)
        db.commit()
        raise HTTPException(status_code=200, detail="Profile deleted")
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


@router.get("/authentication/address/")
def get_address_list(db: Session = Depends(get_db)):
    db_address = db.query(Address).all()
    return db_address


@router.put("/authentication/address/update/", response_model=UpdateAddress)
def update_address(address: UpdateAddress, db: Session = Depends(get_db)):
    try:
        db_address = db.query(Address).filter(Address.id == address.id).first()
        if db_address is None:
            raise HTTPException(status_code=404, detail="Address not found")
        db_address.title = address.title if address.title != "" else db_address.title
        db_address.is_your_receiver_delivery = address.is_your_receiver_delivery
        db_address.phone = address.phone if address.phone != "" else db_address.phone
        db_address.address = (
            address.address if address.address != "" else db_address.address
        )
        db_address.profile_id = (
            address.profile_id if address.profile_id != "" else db_address.profile_id
        )
        db.commit()
        raise HTTPException(status_code=200, detail="Address updated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/authentication/address/delete/", response_model=RemoveAddress)
def remove_address(address: RemoveAddress, db: Session = Depends(get_db)):
    try:
        db_address = db.query(Address).filter(Address.id == address.id).first()
        if db_address is None:
            raise HTTPException(status_code=404, detail="Address not found")
        db.delete(db_address)
        db.commit()
        raise HTTPException(status_code=200,detail="Address deleted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
