from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json 

app = FastAPI()

class Patient(BaseModel):

    name: Annotated[str,Field(...,description='Name of the patient',example='Amaan Sadat')]
    city: Annotated[str,Field(...,description='City of residence',example='Lucknow')]
    gender: Annotated[Literal['male','female','other'],Field(...,description='Gender of the patient',example='male')]
    age: Annotated[int,Field(...,gt=0,lt=100)]
    height: Annotated[float,Field(...,gt=0,strict=True,description='Height of the patient in m',example=1.75)]
    weight: Annotated[float,Field(...,gt=0,strict=True,description='Weight of the patient in kg',example=70.5)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'



def load_data():       
    
    with open('patients.json','r') as f:
        data=json.load(f)
        return data
     
@app.get("/")
def hello():
    return {'message': 'Patients Management'}

@app.get('/about')
def about():
    return{'message' : 'This is a simple API for managing patients in a hospital.'}

@app.get('/view')
def view_patients():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(..., description='ID of patient in DB',example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='Sort on the basis of height,weight,bmi'),order:str=Query('asc',description='sort in ascending or descending order')):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid sort field select from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order select from asc or desc')

    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data 