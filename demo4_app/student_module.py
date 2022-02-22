class Student:
    school_name = None  # static variable or class variable
    school_address = None

    def __init__(self, id, name, percentage):
        self.student_id = id  # non-static variable or instance variable
        self.student_name = name
        self.student_percentage = percentage

    # create a method to print student details
    def print_student_detail(self):
        print("Student Id:", self.student_id)
        print("Student Name:", self.student_name)
        print(self.student_percentage)
        print(Student.school_name)
        print(Student.school_address)
        self.print_result()
        self.print_certification()
        print("*" * 50)

    def print_result(self):
        if self.student_percentage >= 45:
            print("Result:Pass")
        else:
            print("Result:Fail")
        print("*" * 50)

    # create a method (print_grade) for printing grade
    def print_certification(self):
        if self.student_percentage >= 90:
            print(self.student_name," received grade A!! Congrats")
        elif 80 <= self.student_percentage <= 89:
            print(self.student_name, " received grade B!! Congrats")
        elif 60 <= self.student_percentage <= 79:
            print(self.student_name," received grade C!! Congrats")
        elif 45 <= self.student_percentage <= 59:
            print(self.student_name," received grade D!! Congrats")
        else:
            print(self.student_name, " received grade F!! Reattempt!!")
