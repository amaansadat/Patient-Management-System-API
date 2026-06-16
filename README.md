# Patient Management API

A RESTful API built using FastAPI for managing patient records. The API supports CRUD operations, input validation using Pydantic, automatic BMI calculation, patient sorting, and JSON-based data persistence.

## Features

* Create patient records
* View all patients
* View a specific patient by ID
* Update patient information
* Input validation using Pydantic
* BMI calculation using computed fields
* Health verdict generation (Underweight, Normal, Overweight, Obese)
* Sort patients by height, weight, or BMI
* JSON file storage
* Interactive Swagger documentation

## Tech Stack

* Python
* FastAPI
* Pydantic v2
* Uvicorn
* JSON

## API Endpoints

| Method | Endpoint              | Description         |
| ------ | --------------------- | ------------------- |
| GET    | /                     | Home route          |
| GET    | /about                | Project information |
| GET    | /view                 | View all patients   |
| GET    | /patient/{patient_id} | View a patient      |
| GET    | /sort                 | Sort patients       |
| POST   | /create               | Create a patient    |
| PUT    | /edit/{patient_id}    | Update a patient    |

## Patient Schema

* Name
* City
* Gender
* Age
* Height
* Weight
* BMI (Auto Calculated)
* Health Verdict (Auto Generated)

## Installation

```bash
git clone <repository-url>
cd Patient-Management-API
```

Create a virtual environment:

```bash
python -m venv myenv
```

Activate it:

```bash
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

Run the server:

```bash
uvicorn main:app --reload
```

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

## Learning Outcomes

This project demonstrates:

* REST API development with FastAPI
* Data validation with Pydantic
* CRUD operations
* JSON data persistence
* Query and Path parameters
* Error handling using HTTPException
* API documentation using Swagger UI
* Computed fields and business logic implementation
