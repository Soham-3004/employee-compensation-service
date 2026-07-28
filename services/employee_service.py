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