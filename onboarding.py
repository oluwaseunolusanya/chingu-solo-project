"""Module to create an employee account"""
from employee import Employee

name = input("Name of Employee: ")
developer_1 = Employee(name)
print(developer_1.name)
print(developer_1.employee_id)