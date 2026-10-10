from sqlalchemy.orm import Session
import models
import schemas


def create_file(db: Session, file: schemas.FileCreate):
    new_file = models.File(
        file_name=file.file_name,
        content=file.content
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file

def get_all_files(db: Session):
    return db.query(models.File).all()

def get_file_by_id(db: Session, file_id: int):
    return db.query(models.File).filter(models.File.id == file_id).first()

def update_file(db: Session, file_id: int, file: schemas.FileCreate):
    existing_file = db.query(models.File).filter(models.File.id == file_id).first()

    if existing_file:
        existing_file.file_name = file.file_name
        existing_file.content = file.content

        db.commit()
        db.refresh(existing_file)

    return existing_file

def delete_file(db: Session, file_id: int):
    existing_file = db.query(models.File).filter(models.File.id == file_id).first()

    if existing_file:
        db.delete(existing_file)
        db.commit()

    return existing_file

