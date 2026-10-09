# Student Database CRUD API

## Project Overview

This project is a Python backend application developed as part of the EWB internship project assignment. It manages student records using FastAPI and SQLite.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Features

- Create student records
- Retrieve all students
- Retrieve a student by ID
- Filter students by name and course
- Update student details
- Delete student records
- Validate input data
- Handle missing students and duplicate records

## Project Structure

```text
student_crud_app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
├── README.md
└── students.db
```

## Prerequisites

- Python 3.10 or newer
- pip
- Git

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student_crud_app
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

The API will run at:

http://127.0.0.1:8000

## API Documentation

Open Swagger UI:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/students` | Create a student |
| GET | `/students` | List or filter students |
| GET | `/students/{student_id}` | Retrieve a student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Example Student Request

```json
{
  "student_id": 301,
  "name": "Test Student",
  "date_of_birth": "2004-06-15",
  "email": "test301@example.com",
  "phone": "9876543210",
  "course": "B.Tech AIML",
  "address": "Vijayawada",
  "enrollment_date": "2022-08-01"
}
```

## Testing

Use Swagger UI to test all endpoints. Verify successful creation, retrieval, updating, and deletion. Also test invalid input, duplicate IDs or emails, and requests for nonexistent students.

## Security

Use dummy student data for demonstrations. Do not commit passwords, secrets, or real student personal information.

## Future Enhancement

An optional local AI assistant using Ollama could answer natural-language questions about stored student records.

## Author

Add your name here.
