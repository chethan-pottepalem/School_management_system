# app/main.py
# This is the main application file that starts the FastAPI server
# and defines all the API endpoints.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas, models
from .database import get_db, engine

# This command creates all the database tables based on your models.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management API")

# --- School API Endpoints ---
@app.post("/schools/", response_model=schemas.SchoolResponse, tags=["Schools"])
def create_school_api(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.create_school(db=db, school=school)

@app.get("/schools/", response_model=List[schemas.SchoolResponse], tags=["Schools"])
def read_schools_api(db: Session = Depends(get_db)):
    return crud.get_schools(db)

@app.get("/schools/{school_id}", response_model=schemas.SchoolResponse, tags=["Schools"])
def read_school_api(school_id: int, db: Session = Depends(get_db)):
    db_school = crud.get_school(db, school_id=school_id)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school

# --- Standard API Endpoints ---
@app.post("/standards/", response_model=schemas.StandardResponse, tags=["Standards"])
def create_standard_api(standard: schemas.StandardCreate, db: Session = Depends(get_db)):
    return crud.create_standard(db=db, standard=standard)

@app.get("/standards/", response_model=List[schemas.StandardResponse], tags=["Standards"])
def read_standards_api(db: Session = Depends(get_db)):
    return crud.get_standards(db)

# --- Student API Endpoints ---
@app.post("/students/", response_model=schemas.StudentResponse, tags=["Students"])
def create_student_api(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/", response_model=List[schemas.StudentResponse], tags=["Students"])
def read_students_api(db: Session = Depends(get_db)):
    return crud.get_students(db)