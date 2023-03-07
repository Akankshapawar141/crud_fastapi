from pydantic import BaseModel,Field
from uuid import UUID
from fastapi import APIRouter,Depends,HTTPException,status
from app.user import models
from sqlalchemy.orm import Session
from app.user.database import SessionLocal
from app.user.models import CreateUser
from fastapi.encoders import jsonable_encoder

user_route = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    id: UUID
    firstname: str = Field(min_legth=1, max_legth=50)
    lastname: str = Field(min_legth=1, max_legth=50)
    email: str = Field(min_legth=1, max_legth=50)

USER = []

#create user
@user_route.post("/user/")
def Create_user(user: User, db: Session = Depends(get_db)):
    user_model = models.User()
    user_model.firstname = user.firstname
    user_model.lastname = user.lastname
    user_model.email = user.email

    db.add(user_model)
    db.commit()

    return user


#get user
@user_route.get("/user/")
def Get_user(db: Session = Depends(get_db)):
    return db.query(models.User).all()


#Update user
@user_route.put("/user/{user_id}")
def Update_user(user: User, user_id: str, db: Session = Depends(get_db)):

    user_model = db.query(models.User).filter(models.User.id == user_id).first()

    if user_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{user_id} does not found "
        )
    user_model = models.User()
    user_model.firstname = user.firstname
    user_model.lastname = user.lastname
    user_model.email = user.email

    db.add(user_model)
    db.commit()

    return user


@user_route.post("/")
def user_login(user_data: CreateUser):
    result = jsonable_encoder(user_data)
    return result
