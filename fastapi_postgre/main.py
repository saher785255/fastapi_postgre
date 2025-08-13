from fastapi import FastAPI
from fastapi_postgre.client.database import Base, engine
from fastapi_postgre.router import usernames, user_ids, email

app = FastAPI(title="FastAPI + Postgres Sample")

app.include_router(usernames.router)
app.include_router(user_ids.router)
app.include_router(email.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)