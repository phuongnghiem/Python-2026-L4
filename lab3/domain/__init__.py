import numpy as np
class Student:
    def __init__(std,id,name,DoB):
        std.id=id
        std.name=name
        std.DoB=DoB
class Course:
    def __init__(course,id,name,credit):
        course.id=id
        course.name=name
        course.credit=credit
class Mark:
    def __init__(mark,student,course,value):
        mark.student=student
        mark.course=course
        mark.value=value
        

