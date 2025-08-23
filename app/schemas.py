# app/schemas.py
# This file defines the Pydantic models for data validation and shape.
# It ensures the data you receive and send through the API is in the correct format.

from pydantic import BaseModel

# --- School Schemas ---
class SchoolBase(BaseModel):
    name: str
    location: str

class SchoolCreate(SchoolBase):
    pass

class SchoolResponse(SchoolBase):
    id: int

    class Config:
        # Use `from_attributes` instead of `orm_mode` for Pydantic v2
        from_attributes = True

# --- Standard Schemas ---
class StandardBase(BaseModel):
    name: int      # e.g., 1 to 10
    section: str   # e.g., A, B, C

class StandardCreate(StandardBase):
    school_id: int

class StandardResponse(StandardBase):
    id: int
    school_id: int

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

class StudentCreate(StudentBase):
    standard_id: int

class StudentResponse(StudentBase):
    id: int
    standard_id: int

    class Config:
        from_attributes = True