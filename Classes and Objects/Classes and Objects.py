class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student('Negar', 78)
student2 = Student('Abtin', 30)
print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)
did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)

