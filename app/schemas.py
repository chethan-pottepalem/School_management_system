# app/schemas.py
# This file defines the Pydantic models for data validation and shape.
# It ensures the data you receive and send through the API is in the correct format.

from pydantic import BaseModel
from typing import Optional

# --- Teacher Schemas ---
class TeacherBase(BaseModel):
    name: str
    subject: str
    phone : str
    email : str

class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherBase):
    id: int

    class Config:
        # Use `from_attributes` instead of `orm_mode` for Pydantic v2
        from_attributes = True

# --- Standard Schemas ---
class StandardBase(BaseModel):
    name: int      # e.g., 1 to 10
    section: str   # e.g., A, B, C

class StandardUpdate(BaseModel):
    name: Optional[int] = None
    section: Optional[str] = None
    teacher_id: Optional[int] = None


class StandardCreate(StandardBase):
    teacher_id: int

class StandardResponse(StandardBase):
    id: int
    teacher_id: int

    class Config:
        from_attributes = True

# --- Student Schemas ---
class StudentBase(BaseModel):
    name: str
    gender: str
    age: int
    roll_no: int
    phone: str
    marks: int

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    roll_no: Optional[int] = None
    phone: Optional[str] = None
    marks: Optional[int] = None
    standard_id: Optional[int] = None


class StudentCreate(StudentBase):
    standard_id: int

class StudentResponse(StudentBase):
    id: int
    standard_id: int

    class Config:
        from_attributes = True