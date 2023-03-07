from fastapi import FastAPI
from app.user import models
from app.user.database import engine
from app.user.endpoints import user_route


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
print("postgres connected")

app.include_router(user_route,tags=["USERS"])











