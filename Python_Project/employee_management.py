"""
This is a CRUD application for our companies Employee Management System
"""

import sys 
import exceptions 
import employee_list


def main_menu():

    loop = True

    menu_options = {
            1.: 'Add New Employees',
            2.: 'Update Employee Information',
            3.: 'Remove Employee',
            4.: 'List Employee',
            5.: 'Exit'
        }

    while(loop):

        print("Welcome to the Employee Management System!")

        #loop through the menu dictionaries key and display each option using print statements to the console
        for key in menu_options.keys():

            print(key, menu_options[key])

        option = int(input('Enter your choice: \n'))

        try: 
            if option == 1:
                employee_list.Employee.add_employees()
            elif option == 2:
                employee_list.Employee.update_employee(input("Please enter the index of the employee you wish to update: \n"))
            elif option == 3: 
                employee_list.Employee.remove_employee(input("Please enter the index of the employee you wish to remove: \n"))
            elif option == 4:
                employee_list.Employee.list_employees()
            elif option == 5:
                sys.exit(1)
            else:
                print("Invalid option, please enter a number between 1 and 5")

        except ValueError:
            print("Enter a whole number to access the options")
        except Exception:
            print("You did something wrong, not the programs problem")



if __name__ == "__main__":
    main_menu()