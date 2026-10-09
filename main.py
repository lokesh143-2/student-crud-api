
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, Base, SessionLocal


# Initialize FastAPI
app = FastAPI(
    title="Student CRUD API",
    description="API to manage student records using FastAPI and SQLite",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home route
@app.get("/")
def home():
    return {
        "message": "Student CRUD API is running"
    }


# CREATE: Add a new student
@app.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=201
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    # Check whether student ID or email already exists
    existing_student = db.query(models.Student).filter(
        (models.Student.student_id == student.student_id)
        | (models.Student.email == student.email)
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=409,
            detail="Student ID or email already exists"
        )

    return crud.create_student(db, student)


# READ: Get all students, optionally filtered by name or course
@app.get(
    "/students",
    response_model=list[schemas.StudentResponse]
)
def read_students(
    name: str | None = None,
    course: str | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_students(
        db,
        name=name,
        course=course
    )


# READ: Get a student by ID
@app.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# UPDATE: Modify an existing student
@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id: int,
    student_data: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    student = crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Prevent duplicate email addresses
    if student_data.email is not None:
        existing_email = db.query(models.Student).filter(
            models.Student.email == student_data.email,
            models.Student.student_id != student_id
        ).first()

        if existing_email:
            raise HTTPException(
                status_code=409,
                detail="Email already belongs to another student"
            )

    updated_student = crud.update_student(
        db, student_id, student_data
    )

    return updated_student

# DELETE: Remove a student
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.delete_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
