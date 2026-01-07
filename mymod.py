import random
import datetime
import math

def calc(*args):
    total = sum(args)
    avg = total/3
    if (avg > 80):
        Grade = 'A+'
    elif (avg > 60):
        Grade = 'A'
    elif (avg > 40):
        Grade = 'B'
    else:
        Grade = 'F'

    # Generate random student ID
    student_id = random.randint(1000, 9999)

    # Current date and time
    now = datetime.datetime.now()
    date_time = now.strftime("%d-%m-%Y %H:%M:%S")

    print("\n--- Student Report ---")
    print("Student ID:", student_id)
    print("Total Marks:", total)
    print("Average Marks:", math.ceil(avg))
    print("Grade:",Grade)
    print("Report Generated on:", date_time)
