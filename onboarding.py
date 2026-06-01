"""Module to create an employee account"""
from employee.employee import Employee

add_new_employee = 'y'

while add_new_employee == 'y':
    name = input("Name of Employee: ")
    employee = Employee(name)
    employee.role = input("Role: ")
    employee.start_date = input("Employment Started: ")
    print(employee)
    add_new_employee = input("Do you want to add new employee? Enter y or n: ")

print(f"Created {Employee.SIZE} employees.")


