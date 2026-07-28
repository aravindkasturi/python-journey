from employee_model import Employee
from data import data
from employee_manager import EmployeeManger

employee_list=[]
for employee in data:
    employee_name=employee["Name"]
    employee_department=employee["Department"]
    employee_salary=employee["Salary"]
    employee_record=Employee(employee_name,employee_department,employee_salary)
    employee_list.append(employee_record)

employee_manager=EmployeeManger(employee_list)
while employee_manager.has_next_employee():
    employee_manager.display_employee()
    