from utils.db import get_connection

def get_total_bonus():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(Bonus),0) AS TotalBonus
        FROM Employee
    """)

    total_bonus = cursor.fetchone()

    connection.close()

    return total_bonus

def get_employees_with_no_bonus():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM Employee
        WHERE Bonus IS NULL
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees

def get_bonus_percentage():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            EmployeeID,
            FirstName,
            LastName,
            Salary,
            Bonus,
            ROUND((COALESCE(Bonus,0) * 100.0) / Salary, 2) AS BonusPercentage
        FROM Employee
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees

def get_departments_with_high_bonus():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            DepartmentID,
            COALESCE(SUM(Bonus), 0) AS TotalBonus,
            AVG(Salary) AS AverageSalary
        FROM Employee
        GROUP BY DepartmentID
        HAVING COALESCE(SUM(Bonus), 0) > AVG(Salary)
    """)

    departments = cursor.fetchall()

    connection.close()

    return departments

def get_bonus_ranking():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            EmployeeID,
            FirstName,
            LastName,
            Bonus
        FROM Employee
        ORDER BY
            Bonus IS NULL,
            Bonus DESC
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees

def get_highest_salary_employee():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            EmployeeID,
            FirstName,
            LastName,
            Salary,
            Bonus,
            Salary + COALESCE(Bonus, 0) AS TotalCompensation,
            CASE
                WHEN Salary + COALESCE(Bonus, 0) =
                (
                    SELECT MAX(Salary + COALESCE(Bonus, 0))
                    FROM Employee
                )
                THEN 'Yes'
                ELSE 'No'
            END AS HasHighestCompensation
        FROM Employee
        WHERE Salary =
        (
            SELECT MAX(Salary)
            FROM Employee
        )
    """)

    employee = cursor.fetchone()

    connection.close()

    return employee