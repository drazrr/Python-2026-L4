def input_students():
    student_list = []
    students = int(input("Enter the number of students of the class "))
    for i in range(students) :
        student_id = input("Enter the student ID ")
        student_name = str(input("Enter the student name "))
        student_dob = input("Enter DoB: ")

    student = {
        "id" : student_id,
        "name" : student_name,
        "dob": student_dob
    }
    student_list.append(student)

    return student_list

def input_courses():
    course_list = []
    num_course = int(input("Enter the number of courses : "))

    for i in range(num_course):
        course_name = input("Enter the course name : ")
        course_id = int(input("Enter the course id : "))
    courses = {
        "id" : course_id,
        "name": course_name
    }
    course_list.append(courses)

    return course_list
def input_mark(student_list) :
    course_id = int(input("Enter the course id "))
    course_mark = {}

    for student in range(student_list):
        mark = float(input(f"Enter the mark for student {student['name']}(ID: {student['id']}): "))
        course_mark[student['id']] = mark

    return course_id,course_mark

def list_courses(course_list):
        for course in course_list:
             print(f"Course ID :{course['id']} / Name {course['name']}")
             

def list_students(student_list):
        for student in student_list:
             print(f"Student name : {student['name']} / ID {student['id']} / DOB {student['dob']}")

def show_student_mark(course_id,course_mark):
     print(f"Marks for course {course_id['id']}")
     for student_id,mark in course_mark.items():
        print(f"Student ID : {student_id} / Mark : {mark}")

students = input_students()
courses = input_courses()

list_students(students)
list_courses(courses)

course_id,marks = input_mark(students)
show_student_mark(course_id,marks)