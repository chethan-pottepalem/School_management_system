# app/models.py
# This file defines the database tables as Python classes using SQLAlchemy ORM.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base # Import Base from the database file

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # This relationship links a school to its standards.
    standards = relationship("Standard", back_populates="school")

class Standard(Base):
    __tablename__ = "standards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, nullable=False)  # e.g., 1 to 10
    section = Column(String, nullable=False) # e.g., A, B, C
    school_id = Column(Integer, ForeignKey("schools.id"))

    # Relationships to link back to the school and forward to students.
    school = relationship("School", back_populates="standards")
    students = relationship("Student", back_populates="standard")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    roll_no = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)

    standard_id = Column(Integer, ForeignKey("standards.id"))
    # Relationship to link a student to their standard (class).
    standard = relationship("Standard", back_populates="students")