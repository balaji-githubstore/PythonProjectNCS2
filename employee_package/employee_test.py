from employee_package.employee_module import Employee

Employee.print_author()
Employee.company_name = "NCS"
Employee.company_address="Pune"

emp1=Employee(1001,"John",7889.2)
emp2=Employee(1002,"Kenn",9899)

# print(emp1.id)
# print(emp1.name)
# print(emp1.salary)
# print(Employee.company_name)
# print(Employee.company_address)
# print("*"*50)
emp1.print_employee_detail()
emp2.print_employee_detail()

