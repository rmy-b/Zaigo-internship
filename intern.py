# Store student details (name and marks for 3 subjects)
# Use a class called Student
# Use a function to calculate total and average
# Use if / elif / else to decide the grade
# Use a loop to read multiple students
# Use list or dict to store data

#num_students = int(input("Enter number of students: "))
# name = input("Enter Your Name:")
# marks = list(map(int, input("Enter 3 marks separated by comma: ").split(",")))
# for i in range(num_students):
#     name = input(f"\nEnter name of student {i+1}: ")
#     marks = list(map(int, input("Enter 3 marks separated by comma: ").split(",")))
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def total(self):
#         return sum(self.marks)
#     def average(self):
#         return self.total() / len(self.marks)
# S = Student(name,marks)
# print("Sum:",S.total())
# print("Average:", S.average())
#
# if (S.average() > 80):
#     print("Grade: O")
# elif (S.average() > 60):
#     print("Grade: A")
# else:
#     print("Grade: F")


#overrideing
#
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#           print("B")
#
# c = B()
# c.show()
#


#USER DEFINED MODULE

import mymod

name = input("Enter Your Name:")
marks = list(map(int, input("Enter marks separated by comma: ").split(",")))
mymod.calc(*marks)

#ENUMERATE
fruits = ["apple", "banana", "cherry"]

for i, names in enumerate(fruits):
    print(i,names)

#zip()
names = ["hema", "vily", "Chandru"]
marks = ([90, 85, 92],[80,72,85],[65,43,55])

pairs = list(zip(names, marks))
print(pairs)

# for name, mark in zip(names, marks):
#     print(name,mark)

#SORTED
numbers = [32,90,40,80]
print(sorted(numbers))
print(sorted(numbers,reverse=True))

#PDB

import pdb
numbers = [5, 2, 9, 1, 7]
pdb.set_trace()
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
print("Numbers:", numbers)
print("Total:", total, "Max:", maximum, "Min:", minimum)














