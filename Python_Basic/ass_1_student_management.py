import re
import os
import json

script_dir = os.path.dirname(__file__)
rel_path = "data_files/ass_1_student_management.json"
file_path = os.path.join(script_dir, rel_path)

students = {}

def get_student_name():
    student_name = input("Enter a Student Name: ")
    try:
        student_name = str(student_name)
        special_char = re.search("[^a-zA-Z]", student_name)

        if(special_char):
            raise Exception("not valid name")
    except:
        raise Exception("Student name("+student_name+") not valid")
    
    if(not student_name):
        raise Exception("Student name cloud not be Empty")
    return student_name

def get_student_age():
    student_age = input("Enter a Student Age: ")
    try:
        student_age = int(student_age)
        return student_age
    except:
        raise Exception("Student Age("+student_age+") not valid")

def get_student_grade():
    student_grade = input("Enter a Student Grade: ")
    try:
        student_grade = float(student_grade)
        return student_grade
    except:
        raise Exception("Student Grade("+student_grade+") not valid")

def add_student():
    student_name = get_student_name()
    student_age = get_student_age()
    student_grade = get_student_grade()

    if(students[student_name.lower()]):
        print("Student Exist")
        return
    students[student_name.lower()] = {
        "name": student_name,
        "age": student_age,
        "grade": student_grade
    }

def update_grade():
    student_name = get_student_name()
    student_grade = get_student_grade()

    if(not students[student_name.lower()]):
        print("Student does not Exist")
        return
    
    students[student_name.lower()] = {
        "grade": student_grade
    }


def save_students_in_file():
    with open(file_path, 'w') as file:
        json.dump(students, file)

def load_students_from_file():
    global students
    with open(file_path) as file_data:
        students = json.load(file_data)

def calculate_class_avg():
    grades = [student["grade"] for student in students.values()]

    average_grade = sum(grades) / len(grades)
    print("average_grade: ", average_grade)

def find_lowest_highest_grade():
    highest_grade_student = max(students.items(), key=lambda item: item[1]["grade"])
    lowest_grade_student = min(students.items(), key=lambda item: item[1]["grade"])
    print("students.items(): ", students.items())
    print("highest_grade_student: ", highest_grade_student)
    print("lowest_grade_student: ", lowest_grade_student)

def get_menu_option(min_option_num, max_option_num):
    option_num = input("\nEnter a Option: ")
    try:
        option_num = int(option_num)
        if(option_num < min_option_num or option_num > max_option_num):
            raise Exception("Option is out of Range")
        return option_num
    except:
        raise Exception("Option("+str(option_num)+") not valid")
    
def menu():
    print("\n=============================================")
    print("1. Add a new student")
    print("2. Update student grade")
    print("3. View all students")
    print("4. Calculate class average")
    print("5. Find the highest and lowest grades")
    print("6. Save student data to a file")
    print("7. Load student data from a file")
    print("8. Exit the program")

    min_option_num = 1
    max_option_num = 8
    
    return get_menu_option(min_option_num, max_option_num)

def do_operation(option_num):
    if(option_num == 1):
        print("1. Add a new student")
        add_student()
    elif(option_num == 2):
        print("2. Update student grade")
        update_grade()
    elif(option_num == 3):
        print("3. View all students")
        print(students)
    elif(option_num == 4):
        print("4. Calculate class average")
        calculate_class_avg()
    elif(option_num == 5):
        print("5. Find the highest and lowest grades")
        find_lowest_highest_grade()
    elif(option_num == 6):
        print("6. Save student data to a file")
        save_students_in_file()
    elif(option_num == 7):
        print("7. Load student data from a file")
        load_students_from_file()



def main():
    script_continue = True

    while(script_continue):
        try:
            option_num = menu()
        except Exception as error:
            print(error)
            continue

        print("\n------------------OUTPUT---------------------")
        do_operation(option_num)
        print("---------------------------------------------\n")

        if(option_num == 8):
            print("8. Exit the program")
            script_continue = False

main()

# get_menu_option(1, 10)

        
# add_student()
# print(students)