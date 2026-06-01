"""Module to create an employee account"""
from employee.employee import Employee
print("Welcome to Employee Onboarding System")

add_new_employee = 'y'

while add_new_employee == 'y':
    name = input("Enter Name of Employee: ")
    employee = Employee(name)
    employee.role = input("Role: ")
    employee.start_date = input("Employment Started: ")
    print("\n")
    print(employee,"\n")
    add_new_employee = input("Do you want to add new employee? Enter y or n: ")
if Employee.SIZE > 1:
    print(f"Created {Employee.SIZE} employee profiles.")
else:
    print(f"Created {Employee.SIZE} employee profile.")


