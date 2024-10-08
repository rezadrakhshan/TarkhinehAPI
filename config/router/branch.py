from fastapi import APIRouter, Depends, HTTPException
from db.schemas import CreateBranch, UpdateBranch, RemoveBranch
from db.models import Branch
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["Branch"])


@router.post("/branch/create/", response_model=CreateBranch)
def create_branch(branch: CreateBranch, db: Session = Depends(get_db)):
    try:
        db_branch = Branch(
            title=branch.title,
            address=branch.address,
            phone_number=branch.phone_number,
            working_hours=branch.working_hours,
            image=branch.image,
        )
        db.add(db_branch)
        db.commit()
        db.refresh(db_branch)
        return db_branch
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/branch/update/", response_model=UpdateBranch)
def update_branch(branch: UpdateBranch, db: Session = Depends(get_db)):
    try:
        db_branch = db.query(Branch).filter(Branch.id == branch.id).first()
        if db_branch is None:
            raise HTTPException(status_code=404, detail="Branch not found")
        db_branch.title = branch.title if branch.title != "" else db_branch.title
        db_branch.address = (
            branch.address if branch.address != "" else db_branch.address
        )
        db_branch.phone_number = (
            branch.phone_number if branch.phone_number != "" else db_branch.phone_number
        )
        db_branch.working_hours = (
            branch.working_hours
            if branch.working_hours != ""
            else db_branch.working_hours
        )
        db_branch.image = branch.image if branch.image != "" else db_branch.image
        db.commit()
        raise HTTPException(status_code=200, detail="Branch updated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/branch/remove/", response_model=RemoveBranch)
def remove_branch(branch: RemoveBranch, db: Session = Depends(get_db)):
    try:
        db_branch = db.query(Branch).filter(Branch.id == branch.id).first()
        if db_branch is None:
            raise HTTPException(status_code=404, detail="Branch not found")
        db.delete(db_branch)
        db.commit()
        raise HTTPException(status_code=200,detail="Branch was deleted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/branch/")
def get_branch(db:Session = Depends(get_db)):
    try:
        db_branch = db.query(Branch).all()
        return db_branch
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
