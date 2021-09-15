from fastapi import FastAPI, Depends, HTTPException, status
from app import models, database, schemas
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get('/')
def index():
    return 'hello'

