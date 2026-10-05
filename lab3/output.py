import math
import numpy as np
def output_list_course(list_course):
    if len(list_course)==0:
        print("Empty course list")
        return
    print("\n" + "="*40)
    print("          LIST OF COURSE")
    print("="*40)
    print(f"{'ID':<10} | {'Tên môn học':<15} | {'Tín chỉ':<10}")
    print("-" * 40)
    
    for course in list_course:
        print(f"{course.id:<10} | {course.name:<15} | {course.credits:<10}")
    print("="*40)\

def output_list_student(list_std):
    if len(list_std)==0:
            print("Empty student list")
            return
    sorted_std = sorted(list_std, key=lambda student: student.gpa, reverse=True)
    print("\n" + "="*55)
    print("                LIST OF STUDENT")
    print("="*55)
    print(f"{'ID':<10} | {'Name':<15} | {'DoB':<12} | {'GPA':<5}")
    print("-" * 55)
    
    for student in sorted_std:
        print(f"{student.id:<10} | {student.name:<15} | {student.dob:<12} | {student.gpa:<5}")
    print("="*55)

def output_list_mark(list_mark,list_course):
    if len(list_mark) == 0:
        print("No data in system")
        return
    print("List of Course")
    for course in list_course:
        print(f"- ID: {course.id} | Name Course: ")
    selected_course=input("Enter course you want see mark")
    print("\n" + "="*40)
    print(f"      MARK TABLE: {selected_course}")
    print("="*40)
    print(f"{'ID student':<15} | {'Name':<15} | {'Mark':<5}")
    print("-" * 40)
    found = False
    for mark in list_mark:
        if mark.course.id == selected_course:
            print(f"{mark.student.id:<15} | {mark.student.name:<15} | {mark.value:<5}")
            found = True 
    if not found:
        print(f"No data in system {selected_course}.")
    print("="*40)