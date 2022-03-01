from unicodedata import name
import uuid
import pprint

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

        except: 
            pass
        
    def update_employee(id):

        # if employee obj id == id then .update values with new user inputs

        try:

            id = input("Please enter the ID of the employee you wish to update: \n")

            for employee in Employee.employee_details:
                if employee.id == id:
                    
                #access the current employee object and set a new user input value for each field
                    employee.first_name = input("Enter your first name: \n")
                    employee.last_name = input("Enter your last name: \n")
                    employee.date_of_employment = input("Enter your last date of employment: \n")
                    employee.salary = input("Enter your salary: \n")
                    employee.department = input("Enter your department: \n")

        except: 
            pass

    def remove_employee(id):
        pass

    def list_employees():

        for employee in Employee.employee_details:
            print(f"Employee ID: {employee.id}\nEmployee First Name: {employee.first_name}\nEmployee Last Name: {employee.last_name}\nDOE: {employee.date_of_employment}\nSalary : {employee.salary}\nDepartment : {employee.department}\n ******************** ")

        