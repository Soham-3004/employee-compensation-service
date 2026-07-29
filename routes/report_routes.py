import azure.functions as func
import json
from app import app

from services.report_service import(
    get_total_bonus,
    get_employees_with_no_bonus,
    get_bonus_percentage,
    get_departments_with_high_bonus,
    get_bonus_ranking,
    get_highest_salary_employee
)

@app.route(route="reports/total-bonus",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_total_bonus_endpoint(req: func.HttpRequest):

    result = get_total_bonus()

    return func.HttpResponse(
        json.dumps(dict(result)),
        status_code=200,
        mimetype="application/json"
    )

@app.route(
    route="reports/no-bonus",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS
)
def get_no_bonus_employees_endpoint(req: func.HttpRequest):

    employees = get_employees_with_no_bonus()

    employees_data = []

    for employee in employees:
        employees_data.append(dict(employee))

    return func.HttpResponse(
        json.dumps(employees_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="reports/bonus-percentage",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_bonus_percentage_endpoint(req: func.HttpRequest):

    employees = get_bonus_percentage()

    employees_data = []

    for employee in employees:
        employees_data.append(dict(employee))

    return func.HttpResponse(
        json.dumps(employees_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="reports/high-bonus-departments",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_high_bonus_departments_endpoint(req: func.HttpRequest):

    departments = get_departments_with_high_bonus()

    departments_data = []

    for department in departments:
        departments_data.append(dict(department))

    return func.HttpResponse(
        json.dumps(departments_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="reports/bonus-ranking",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_bonus_ranking_endpoint(req: func.HttpRequest):

    employees = get_bonus_ranking()

    employees_data = []

    for employee in employees:
        employees_data.append(dict(employee))

    return func.HttpResponse(
        json.dumps(employees_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="reports/highest-compensation",methods=["GET"],auth_level=func.AuthLevel.ANONYMOUS)
def get_highest_compensation_endpoint(req: func.HttpRequest):

    employee = get_highest_salary_employee()

    return func.HttpResponse(
        json.dumps(dict(employee)),
        status_code=200,
        mimetype="application/json"
    )