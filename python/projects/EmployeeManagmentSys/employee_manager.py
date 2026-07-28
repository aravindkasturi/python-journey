class EmployeeManger:
    def __init__(self,employee_list):
        self.employee_list=employee_list
        self.current_employee=0
    def has_next_employee(self):
        return self.current_employee<len(self.employee_list)
    def calculate_bonus(self):
        employee=self.employee_list[self.current_employee]
        if employee.salary>90000:
            return "High"
        elif employee.salary >= 60000:
            return "Medium"
        else:
            return "low"
    def display_employee(self):
        employee=self.employee_list[self.current_employee]
        print(f"Employee Name: {employee.name}")
        print(f"Department: {employee.department}")
        print(f"Salary: {employee.salary}")
        a=self.calculate_bonus()
        print(f"Bonus: {a}")
        self.current_employee+=1
        print("\n")