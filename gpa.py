## gpa calculator
import sqlite3

student_grades =sqlite3.connect("grades.db")


grades = [99,99,90,99]

def gpa_calculator(g):
    gpa = 0
    for i in g:
        gpa += ((i - 60)/10)
    gpa = gpa/4

    return gpa

print(gpa_calculator(grades))