from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class Employee(BaseModel):
    name: str
    age: int
    position: str

employees = []

@app.post('/employee')
def post_employee(employee: Employee):
    # Generate a unique ID for the new employee
    employee_id = uuid4()
    # Append the new employee to the list
    employees.append({'employee_id': employee_id, 'employee': employee})
    # Return the created employee details
    return {'employee_id': employee_id, 'employee': employee}

@app.get('/employee/{employee_id}')
def get_employee(employee_id: UUID):
    # Find the employee by ID
    for emp in employees:
        if emp['employee_id'] == employee_id:
            return emp
    # Raise 404 error if not found
    raise HTTPException(status_code=404, detail='Employee not found')

@app.get('/employees')
def get_employees():
    # Return all employees
    return {'employees': employees}

@app.delete('/employee/{employee_id}')
def delete_employee(employee_id: UUID):
    # Find the employee by ID
    for index, emp in enumerate(employees):
        if emp['employee_id'] == employee_id:
            # Remove the employee from the list
            del employees[index]
            return {'message': 'Employee deleted successfully'}
    # Raise 404 error if not found
    raise HTTPException(status_code=404, detail='Employee not found')

@app.put('/employee/{employee_id}')
def update_employee(employee_id: UUID, updated_employee: Employee):
    # Find the employee by ID
    for emp in employees:
        if emp['employee_id'] == employee_id:
            # Update the employee details
            emp['employee'] = updated_employee
            return {'employee_id': employee_id, 'employee': updated_employee}
    # Raise 404 error if not found
    raise HTTPException(status_code=404, detail='Employee not found')
