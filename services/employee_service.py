from utils.db import get_connection

def create_employee(first_name, last_name, department_id, salary, bonus, hire_date):
    connection = get_connection()   #connect to db
    cursor = connection.cursor()    #object that runs the sql query
    cursor.execute(                 #exec insert
        """
        INSERT INTO Employee
        (
            FirstName,
            LastName,
            DepartmentID,
            Salary,
            Bonus,
            HireDate
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            first_name,
            last_name,
            department_id,
            salary,
            bonus,
            hire_date
        ))  #? are placeholders which get replaced by the values passed while execution

    connection.commit() #exec the sql stmt
    employee_id = cursor.lastrowid  #get last row from db
    connection.close()  #close connection 

    return employee_id  #return the created employee

def get_employee_by_id(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
            SELECT
                EmployeeID,
                FirstName,
                LastName,
                DepartmentID,
                Salary,
                COALESCE(Bonus, ROUND(Salary * 0.05, 2)) AS Bonus,
                HireDate
            FROM Employee
            WHERE EmployeeID = ?;
        """,
        (employee_id,)
    )
    employee = cursor.fetchone()
    connection.close()
    return employee

def get_all_employees(department_id = None):
    connection = get_connection()
    cursor = connection.cursor()

    if department_id is None:
        cursor.execute(
            """
            SELECT
                EmployeeID,
                FirstName,
                LastName,
                DepartmentID,
                Salary,
                COALESCE(Bonus, ROUND(Salary * 0.05, 2)) AS Bonus,
                HireDate
            FROM Employee;
            """
            )
    else:
        cursor.execute(
            """
            SELECT * FROM Employee WHERE DepartmentID = ?
            """,
            (department_id,)
        )
        
    employees = cursor.fetchall()
    connection.close()        
    return employees

def update_employee(employee_id,first_name, last_name, department_id, salary, bonus, hire_date):
    connection = get_connection()  
    cursor = connection.cursor()   
    cursor.execute(                 
        """
        UPDATE Employee
        SET
            FirstName = ?,
            LastName = ?,
            DepartmentID = ?,
            Salary = ?,
            Bonus = ?,
            HireDate = ?
        WHERE EmployeeID = ?
        """,
        (
            first_name,
            last_name,
            department_id,
            salary,
            bonus,
            hire_date,
            employee_id
        )) 

    connection.commit() 
    rows_updated = cursor.rowcount
    connection.close()   

    return rows_updated   

def delete_employee(employee_id):
    connection = get_connection()  
    cursor = connection.cursor()   
    cursor.execute(                 
        """
        DELETE FROM Employee WHERE EmployeeID = ?
        """,
        (employee_id,)
    )       
    connection.commit() 
    rows_deleted = cursor.rowcount
    connection.close()   
    return rows_deleted