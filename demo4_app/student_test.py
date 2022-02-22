from demo4_app import student_module

student_module.Student.school_name = "Global School"
student_module.Student.school_address = "#23 Chennai-34"

stu1 = student_module.Student(101, "John", 78.2)

stu2 = student_module.Student(102, "Peter", 58.2)

stu3 = student_module.Student(103, "ken", 85)
# create Student object and load (103,ken,98.2)

print(type(stu1))
print(stu2.student_id)
print(stu2.student_name)
print(stu2.student_percentage)
print(student_module.Student.school_name)
print(student_module.Student.school_address)
print("*" * 50)


print(stu1)
print(stu2)
print(stu3)
