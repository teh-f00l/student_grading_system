def grades():
    grades = int(input(student.subject))
    if 100 <= grades >= 90:
        print ("Subject  A")
    elif grades >= 80:
        print ("Subject  B")
    elif grades >= 70:
        print ("Subject C")
    else:
        print ("Subject F")
grades()