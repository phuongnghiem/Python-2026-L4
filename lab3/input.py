from domain import Student
from domain import Course
from domain import Mark
import numpy as np
import math
def input_student():
    number_std=int(input("Enter the number of student: "))
    list_std=[]
    for i in range(number_std):
        print(f"Enter infomation of student {i+1}: ")
        s_id= input("Enter the id: ")
        s_name= input("Enter the name: ")
        s_dob = input("Enter the Date of Birth: ")
        new_student=Student(s_id,s_name,s_dob)
        list_std.append(new_student)
    return list_std
def input_course():
    number_course=int(input("Enter the number of course"))
    list_course=[]
    for i in range(number_course):
        print(f"Enter information of course: ")
        c_id=input("Enter the id: ")
        c_name= input("Enter the name: ")
        c_credit=input("Enter the credit of course")
        new_course=Course(c_id,c_name,c_credit)
        list_course.append(new_course)
    return list_course
def input_mark(list_std,list_course):
    if len(list_std) == 0 or len(list_course) == 0:
        print("Error")
        return []
    print("List of course: ")
    for course in list_course:
        print(f"- ID: {course.id} | Name Course: {course.name}")   

    selected_c_id = input("\nEnter the id of course: ")
    selected_course = None
    for course in list_course:
        if course.id == selected_c_id:
            selected_course = course
            break
    if selected_course is None:
        print("Error! Cant find your course")
        return []
    print(f"\n--- Enter mark in {selected_course.name} ---")
    list_marks = []
    
    for student in list_std:
        raw_mark = float(input(f"Mark of {student.name} (ID: {student.id}): "))
        rounded_mark = math.floor(raw_mark * 10) / 10 
        new_mark = Mark(student, selected_course, rounded_mark)
        list_marks.append(new_mark)      
    print("\nEnter mark successful")
    return list_marks




