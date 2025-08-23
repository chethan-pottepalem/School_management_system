# app/crud.py
# This file contains all the CRUD (Create, Read, Update, Delete)
# functions that interact directly with the database.

from sqlalchemy.orm import Session
from . import models, schemas

# --- School CRUD Functions ---
def get_school(db: Session, school_id: int):
    return db.query(models.School).filter(models.School.id == school_id).first()

def get_schools(db: Session):
    return db.query(models.School).all()

def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(name=school.name, location=school.location)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

# --- Standard CRUD Functions ---
def get_standard(db: Session, standard_id: int):
    return db.query(models.Standard).filter(models.Standard.id == standard_id).first()

def get_standards(db: Session):
    return db.query(models.Standard).all()

def create_standard(db: Session, standard: schemas.StandardCreate):
    db_standard = models.Standard(**standard.model_dump())
    db.add(db_standard)
    db.commit()
    db.refresh(db_standard)
    return db_standard

# --- Student CRUD Functions ---
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student