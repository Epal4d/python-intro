#Initialize empty dictionary
student_grades = {}

#function to add a student and their grade to dictionary
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' has been added with a '{grade}' grade.")

#function to remove a student from dictionary 
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"student '{name}' has been deleted")
    else:
        print(f"student {name} not found")

#function to Display All students and their grades
def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student: '{name}' grade has been updated to '{grade}'")
    else:
        print(f"Name '{name}' Not found")

def find_grade(name):
    if name in student_grades:
        grade = student_grades[name]
        print(f"'{name}' has a grade of -'{grade}'")
    else:
        print(f"Student '{name}' not found")

#calculate average of all students in the dictionary
def average_grade():
    total = 0
    for grade in student_grades.values():
        total = total + grade
    average = total / len(student_grades)
    print(f"The average of all the grade in the class is '{average}'")
        

    

#Adding students 
add_student("Evan", 95)
add_student("Sarah", 88)
add_student("Marcus", 91)
add_student("Lena", 84)

#display students
display_students()

#update student's grades
update_grade("Sarah",75)
update_grade("Jim", 100)
update_grade("Lena", 93)

#remove students
remove_student("Marcus")

#Display students again
display_students()

find_grade("Evan")

average_grade()

