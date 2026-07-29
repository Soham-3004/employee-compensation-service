import azure.functions as func # type: ignore #import azure functions
import datetime 
import json
import logging
from services.employee_service import create_employee, get_employee_by_id, get_all_employees, update_employee, delete_employee

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


@app.route(route="employees/{id:int}",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_employee_by_id_endpoint(req: func.HttpRequest):
    employee_id = int(req.route_params.get("id"))
    employee = get_employee_by_id(employee_id)
    if employee is None:
        return func.HttpResponse(json.dumps({"message": "Employee not found"}),
            status_code=404,
            mimetype="application/json"
        )
    else:
        employee_data = dict(employee)
        return func.HttpResponse(json.dumps(employee_data),
            status_code=200,
            mimetype="application/json"
        )

@app.route(route="employees",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_all_employees_endpoint(req: func.HttpRequest):
    department = req.params.get("department")
    if department is not None:
        try:
            department = int(department)
        except ValueError:
            return func.HttpResponse("Department must be an Integer", status_code = 400)
        
    employees = get_all_employees(department)
    employees_data = []
    for employee in employees:
        employees_data.append(dict(employee))

    return func.HttpResponse(
        json.dumps(employees_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="employees/{id:int}",methods=["PUT"],auth_level=func.AuthLevel.ANONYMOUS)
def update_employee_endpoint(req: func.HttpRequest):
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON",status_code = 400)

    employee_id = int(req.route_params.get("id"))
    first_name = data.get("FirstName")
    last_name = data.get("LastName")
    department_id = data.get("DepartmentID")
    salary = data.get("Salary")
    bonus = data.get("Bonus")
    hire_date = data.get("HireDate")

    if not all([first_name, last_name, department_id, salary, bonus, hire_date]):
        return func.HttpResponse("Missing fields",status_code = 400)
    
    rows_updated = update_employee(employee_id,first_name, last_name, department_id, salary, bonus, hire_date)

    if rows_updated == 0:
        return func.HttpResponse(json.dumps({"message": "Employee not found"}),
            status_code=404,
            mimetype="application/json"
        )
    else:
        return func.HttpResponse(json.dumps({"message": "Employee Updated Successfully"}),
            status_code=200,
            mimetype="application/json"
        )

@app.route(route="employees/{id:int}", methods=["DELETE"], auth_level=func.AuthLevel.ANONYMOUS)
def delete_employee_endpoint(req: func.HttpRequest):
    employee_id = int(req.route_params.get("id"))
    rows_deleted = delete_employee(employee_id)
    if rows_deleted == 0:
        return func.HttpResponse(json.dumps({"message": "Employee not found"}),
            status_code=404,
            mimetype="application/json"
        )   
    else:
        return func.HttpResponse(json.dumps({"message": "Employee Deleted Successfully"}),
            status_code=200,
            mimetype="application/json"
        )            