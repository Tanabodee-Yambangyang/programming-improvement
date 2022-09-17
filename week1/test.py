"""Compare module, dictionary and class"""
import employee
from employee_cls import Employee


# using dictionary to get EmployeID

employee_dic = {"EmployeID": "Employee Unique Identity!"}
print(employee_dic["EmployeID"])

# using function and variable from employee module

employee. employee_id()
print(employee.Age)

# using method and attribute from Employee class

employee_obj = Employee()
employee_obj.get_id()
print(employee_obj.age)