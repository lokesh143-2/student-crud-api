
from sqlalchemy.orm import Session
import models
import schemas


# CREATE: Add a student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# READ: Get all students with optional filters
def get_students(db: Session, name=None, course=None):
    query = db.query(models.Student)

    if name:
        query = query.filter(
            models.Student.name.ilike(f"%{name}%")
        )

    if course:
        query = query.filter(
            models.Student.course.ilike(f"%{course}%")
        )

    return query.order_by(models.Student.student_id).all()


# READ: Get one student by ID
def get_student_by_id(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.student_id == student_id)
        .first()
    )


# UPDATE: Update an existing student
def update_student(
    db: Session,
    student_id: int,
    student_data: schemas.StudentUpdate
):
    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    update_data = student_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student
