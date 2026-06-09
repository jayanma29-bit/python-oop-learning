class Student:

    def __init__(self, name, grade=None):
        self.grade = grade
        self.name = name

    def __repr__(self):
        return f"Student: {self.name} | Grade: {self.grade}"
    
    def get_grade_letter(self):
        grade = self.grade
       
        if grade >= 90:
            return "A"
        
        elif grade >= 80:
            return "B"
        
        elif grade >= 70:
            return "C"
        
        elif grade >= 60:
            return "D"
        
        elif grade < 60:
            return "F"
    
    def get_grade_number(self):
        return self.grade
        

class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = {}

    def __repr__(self):
        return f"Teacher: {self.name} | Subject: {self.subject} | Students: {len(self.students)}"
    

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name, None)
        elif name in self.students:
            print(f"{name} is already in the class.")
    
    def add_grade(self, name, grade):

        if grade < 0 or grade > 100:
            print("Invalid grade. Please enter a grade between 0 and 100.")


        elif name in self.students:
            self.students[name].grade = grade
            print(f"{name}'s grade set to {grade}.")


        elif name not in self.students:
            print(f"{name} is not in the class. Please add the student before assigning a grade.")

    def class_average(self):
        total = 0
        count = 0
        for student in self.students.values():
            if student.grade is not None:
                total += student.grade
                count += 1

        if count == 0:
            return 0
        return total / count
    
    def top_student(self):
        top_student = None
        highest_grade = -1

        for student in self.students.values():
            if student.grade is not None and student.grade > highest_grade:
                highest_grade = student.grade
                top_student = student

        return top_student
    

    def failing_students(self):
        failing_students = []
        for student in self.students.values():
            if student.grade is not None and student.grade < 60:
                failing_students.append(student)
        
        return failing_students
    


teacher = Teacher("Brooks", "Math")

teacher.add_student("Declan")
teacher.add_student("Jayan")
teacher.add_student("Bao")

teacher.add_grade("Declan", 95)
teacher.add_grade("Jayan", 100)
teacher.add_grade("Bao", 70)

teacher.add_student("Declan") # this should be rejected since declan is already in the class
teacher.add_grade("Alice", 85) # this should be rejected since alice is not in the class
teacher.add_grade("Bao", 105) # this should be rejected since the grade is too high
teacher.add_grade("Bao", -5) # this should be rejected since the grade is too low

print(teacher.students["Bao"].get_grade_letter()) # should print C

print(teacher.students["Bao"].get_grade_number())


