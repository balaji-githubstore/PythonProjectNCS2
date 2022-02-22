class Student:
    school_name = None  # static variable or class variable
    school_address = None

    def __init__(self, id, name, percentage):
        self.student_id = id  # non-static variable or instance variable
        self.student_name = name
        self.student_percentage = percentage
