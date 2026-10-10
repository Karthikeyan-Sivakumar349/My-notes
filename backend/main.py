from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine, SessionLocal

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "File Manager API is running successfully!"}


@app.post("/files", response_model=schemas.FileResponse)
def create_file(file: schemas.FileCreate, db: Session = Depends(get_db)):
    return crud.create_file(db, file)

@app.get("/files", response_model=list[schemas.FileResponse])
def get_files(db: Session = Depends(get_db)):
    return crud.get_all_files(db)

@app.get("/files/{file_id}", response_model=schemas.FileResponse)
def get_file(file_id: int, db: Session = Depends(get_db)):
    return crud.get_file_by_id(db, file_id)

@app.put("/files/{file_id}", response_model=schemas.FileResponse)
def update_file(file_id: int, file: schemas.FileCreate, db: Session = Depends(get_db)):
    return crud.update_file(db, file_id, file)

@app.delete("/files/{file_id}", response_model=schemas.FileResponse)
def delete_file(file_id: int, db: Session = Depends(get_db)):
    return crud.delete_file(db, file_id)