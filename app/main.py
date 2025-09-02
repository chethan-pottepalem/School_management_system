# models.py
# This file defines the database structure for the School Management System using SQLAlchemy ORM.
# 
# - Teacher: Represents the school (Viswabharathi High School) and stores basic info.
# - Standard: Represents a class/grade and section, linked to a teacher.
# - Student: Represents a student, linked to a standard.
#
# All standards and students are associated with the default school ("Viswabharathi High School") via the Teacher model.
# Relationships are set up so that:
#   - A Teacher can have many Standards.
#   - A Standard can have many Students.
#   - Each Student belongs to one Standard.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas, models
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management API")

# --- Teacher API Endpoints ---
@app.post("/teachers/", response_model=schemas.TeacherResponse, tags=["Teachers"])
def create_teacher_api(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, teacher=teacher)

@app.get("/teachers/", response_model=List[schemas.TeacherResponse], tags=["Teachers"])
def read_teachers_api(db: Session = Depends(get_db)):
    return crud.get_teachers(db)

@app.get("/teachers/{teacher_id}", response_model=schemas.TeacherResponse, tags=["Teachers"])
def read_teacher_api(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.put("/teachers/{teacher_id}", response_model=schemas.TeacherResponse, tags=["Teachers"])
def update_teacher_put_api(teacher_id: int, teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = crud.update_teacher_put(db=db, teacher_id=teacher_id, teacher=teacher)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

# --- Teacher PATCH API (Partial Update) ---
@app.patch("/teachers/{teacher_id}", response_model=schemas.TeacherResponse, tags=["Teachers"])
def update_teacher_patch_api(teacher_id: int, teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    db_teacher = crud.update_teacher_patch(db=db, teacher_id=teacher_id, teacher=teacher)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher


@app.delete("/teachers/{teacher_id}", tags=["Teachers"])
def delete_teacher_api(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    crud.delete_teacher(db, teacher_id=teacher_id)
    return {"msg": f"Teacher with ID {teacher_id} deleted successfully"}


# --- Standard API Endpoints ---
@app.post("/standards/", response_model=schemas.StandardResponse, tags=["Standards"])
def create_standard_api(standard: schemas.StandardCreate, db: Session = Depends(get_db)):
    return crud.create_standard(db=db, standard=standard)

@app.get("/standards/", response_model=List[schemas.StandardResponse], tags=["Standards"])
def read_standards_api(db: Session = Depends(get_db)):
    return crud.get_standards(db)

@app.put("/standards/{standard_id}", response_model=schemas.StandardResponse, tags=["Standards"])
def update_standard_put_api(standard_id: int, standard: schemas.StandardCreate, db: Session = Depends(get_db)):
    db_standard = crud.update_standard_put(db=db, standard_id=standard_id, standard=standard)
    if db_standard is None:
        raise HTTPException(status_code=404, detail="Standard not found")
    return db_standard

@app.patch("/standards/{standard_id}", response_model=schemas.StandardResponse, tags=["Standards"])
def update_standard_patch_api(standard_id: int, standard: schemas.StandardUpdate, db: Session = Depends(get_db)):
    db_standard = crud.update_standard_patch(db=db, standard_id=standard_id, standard=standard)
    if db_standard is None:
        raise HTTPException(status_code=404, detail="Standard not found")
    return db_standard

@app.delete("/standards/{standard_id}", tags=["Standards"])
def delete_standard_api(standard_id: int, db: Session = Depends(get_db)):
    db_standard = crud.get_standard(db, standard_id=standard_id)
    if db_standard is None:
        raise HTTPException(status_code=404, detail="Standard not found")
    crud.delete_standard(db, standard_id=standard_id)
    return {"msg": f"Standard with ID {standard_id} deleted successfully"}

# --- Student API Endpoints ---
@app.post("/students/", response_model=schemas.StudentResponse, tags=["Students"])
def create_student_api(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/", response_model=List[schemas.StudentResponse], tags=["Students"])
def read_students_api(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.put("/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"])
def update_student_put_api(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student_put(db=db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.patch("/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"])
def update_student_patch_api(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.update_student_patch(db=db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}", tags=["Students"])
def delete_student_api(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_student(db, student_id=student_id)
    return {"msg": f"Student with ID {student_id} deleted successfully"}