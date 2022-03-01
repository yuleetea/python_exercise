from unicodedata import name
import uuid
import pprint
from Python_Project.exceptions import not_a_department_exception
import exceptions

class Employee:

    employee_details = []

    def __init__(self, first_name: str, last_name: str, date_of_employment: str, salary: int, department: str, id = uuid.uuid4()):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_employment = date_of_employment
        self.salary = salary
        self.department = department
        self.id = id


    #adds the created employee to the employee_details list
    def add_employees():
        
        try:
            #creates an employee object
            first_name = input("Enter your first name: \n")
            last_name = input("Enter your last name: \n")
            date_of_employment = input("Enter your last date of employment: \n")
            salary = input("Enter your salary: \n")
            department = input("Enter your department: \n")

            # employee_obj = Employee({'First name' : first_name, 'Last name' : last_name, 'Date of Employment' : date_of_employment, 'Salary': salary, 'Department': department })

            employee_obj = Employee(first_name=first_name, last_name=last_name, date_of_employment=date_of_employment, salary=salary, department=department)
            
            Employee.employee_details.append(employee_obj)

        except not_a_department_exception: 
            print("Did not enter a department")
        
    def update_employee(index):

        # if employee obj id == id then .update values with new user inputs

        try:

            option = int(index)

            employee = Employee.employee_details[option]
                    
            #access the current employee object and set a new user input value for each field
            employee.first_name = input("Enter your first name: \n")
            employee.last_name = input("Enter your last name: \n")
            employee.date_of_employment = input("Enter your last date of employment: \n")
            employee.salary = input("Enter your salary: \n")
            employee.department = input("Enter your department: \n")

        except ValueError: 
            print("Index must be an integer")

    #pop 
    def remove_employee(index):

        try:

            option = int(index)

            Employee.employee_details.pop(option)
                    

        except ValueError: 
            print("Index must be an integer")

        except IndexError:
            print("Sequence index out of range")


    def list_employees():

        for employee in Employee.employee_details:
            print(f"Employee ID: {employee.id}\nEmployee First Name: {employee.first_name}\nEmployee Last Name: {employee.last_name}\nDOE: {employee.date_of_employment}\nSalary : {employee.salary}\nDepartment : {employee.department}\n ******************** ")

        