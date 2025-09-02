# app/crud.py
# This file contains all the CRUD (Create, Read, Update, Delete)
# functions that interact directly with the database.

from sqlalchemy.orm import Session
from . import models, schemas

# --- Teachers CRUD Functions ---
def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def get_teachers(db: Session):
    return db.query(models.Teacher).all()

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def update_teacher_put(db: Session, teacher_id: int, teacher: schemas.TeacherCreate):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not db_teacher:
        return None
    for key, value in teacher.dict().items():
        setattr(db_teacher, key, value)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def update_teacher_patch(db: Session, teacher_id: int, teacher: schemas.TeacherUpdate):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not db_teacher:
        return None
    for key, value in teacher.dict(exclude_unset=True).items():
        setattr(db_teacher, key, value)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if teacher:
        db.delete(teacher)
        db.commit()


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

def update_standard_put(db: Session, standard_id: int, standard: schemas.StandardCreate):
    db_standard = db.query(models.Standard).filter(models.Standard.id == standard_id).first()
    if not db_standard:
        return None
    for key, value in standard.dict().items():
        setattr(db_standard, key, value)
    db.commit()
    db.refresh(db_standard)
    return db_standard

def update_standard_patch(db: Session, standard_id: int, standard: schemas.StandardUpdate):
    db_standard = db.query(models.Standard).filter(models.Standard.id == standard_id).first()
    if not db_standard:
        return None
    for key, value in standard.dict(exclude_unset=True).items():
        setattr(db_standard, key, value)
    db.commit()
    db.refresh(db_standard)
    return db_standard

def delete_standard(db: Session, standard_id: int):
    standard = db.query(models.Standard).filter(models.Standard.id == standard_id).first()
    if standard:
        db.delete(standard)
        db.commit()

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

def update_student_put(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        return None
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student_patch(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        return None
    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()