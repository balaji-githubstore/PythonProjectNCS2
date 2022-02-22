class Employee:
    company_name = None  # static variable or class variable
    company_address = None

    def __init__(self, id, name, salary):
        self.id = id  # non-static variable or instance variable
        self.name = name
        self.salary = salary

    def print_employee_detail(self):
        print(self.id)
        print(self.name)
        print(self.salary)
        print(Employee.company_name)
        print(Employee.company_address)
        print("*" * 50)
