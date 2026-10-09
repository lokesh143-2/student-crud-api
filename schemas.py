
from datetime import date
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    field_validator,
    model_validator
)


# ==========================================
# CREATE STUDENT SCHEMA
# ==========================================

class StudentCreate(BaseModel):

    student_id: int = Field(gt=0)

    name: str = Field(min_length=2, max_length=100)

    date_of_birth: date

    email: EmailStr

    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=20
    )

    course: Optional[str] = Field(
        default=None,
        max_length=100
    )

    address: Optional[str] = Field(
        default=None,
        max_length=200
    )

    enrollment_date: Optional[date] = None

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value):
        if value > date.today():
            raise ValueError(
                "Date of birth cannot be in the future"
            )
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if value is not None and not value.isdigit():
            raise ValueError(
                "Phone number must contain only digits"
            )
        return value


# ==========================================
# UPDATE STUDENT SCHEMA
# ==========================================

class StudentUpdate(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    date_of_birth: Optional[date] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=20
    )

    course: Optional[str] = Field(
        default=None,
        max_length=100
    )

    address: Optional[str] = Field(
        default=None,
        max_length=200
    )

    enrollment_date: Optional[date] = None

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value):
        if value is not None and value > date.today():
            raise ValueError(
                "Date of birth cannot be in the future"
            )
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if value is not None and not value.isdigit():
            raise ValueError(
                "Phone number must contain only digits"
            )
        return value

    @model_validator(mode="after")
    def validate_required_fields(self):
        for field in ("name", "date_of_birth", "email"):
            if (
                field in self.model_fields_set
                and getattr(self, field) is None
            ):
                raise ValueError(
                    f"{field} cannot be null"
                )
        return self


# ==========================================
# STUDENT RESPONSE SCHEMA
# ==========================================

class StudentResponse(BaseModel):

    student_id: int

    name: str

    date_of_birth: date

    email: EmailStr

    phone: Optional[str] = None

    course: Optional[str] = None

    address: Optional[str] = None

    enrollment_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)
