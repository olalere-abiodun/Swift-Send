from fastapi import FastAPI
from app import models
from app.database import engine

from app.routers import users, auth, addresses

from app.routers import users, auth, packages, delivery


# for pushing tables to the database. comment this out if you are using alembic
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(users.router)

app.include_router(addresses.router)

app.include_router(packages.router)
app.include_router(delivery.router)



@app.get("/")
async def root():
    return {"message": "Welcome to the Swift Send API!"}
