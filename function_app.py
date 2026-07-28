import azure.functions as func #import azure functions
import datetime 
import json
import logging
from services.employee_service import create_employee

app = func.FunctionApp()    #Create the main app object and add endpoints to it 

@app.route(route="employees",methods=["POST"],auth_level=func.AuthLevel.ANONYMOUS)
def create_employee_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON",status_code = 400)
    
    first_name = data.get("FirstName")
    last_name = data.get("LastName")
    department_id = data.get("DepartmentID")
    salary = data.get("Salary")
    bonus = data.get("Bonus")
    hire_date = data.get("HireDate")

    if not all([first_name, last_name, department_id, salary]):
        return func.HttpResponse("Missing fields",status_code = 400)
    
    employee_id = create_employee(first_name, last_name, department_id, salary, bonus, hire_date)

    return func.HttpResponse(
    json.dumps({
        "EmployeeID": employee_id,
        "message": "Employee created successfully"
    }),
    status_code=201,
    mimetype="application/json"
    )