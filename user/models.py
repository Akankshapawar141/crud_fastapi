from sqlalchemy import Integer,String,Column
from app.user.database import Base
from pydantic import BaseModel,Field
import uuid




class User(Base):
    __tablename__ = "User"

    id =Column(Integer,primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)


class CreateUser(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    firstname: str = Field(...)
    lastname: str = Field(...)
    email :str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 101,
                "firstname": "Akanksha ",
                "lastname": "pawar",
                "email": "akankshapawar141@gamil.com",
            }
        }

