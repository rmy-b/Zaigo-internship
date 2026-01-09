#You are given a list where 1 = present, 0 = absent.
# Count total present days
# Count total absent days

attend = list((1,0,1,1,0,0,1))
present = 0
absent = 0
for i in range(len(attend)):
    if (attend[i]) == 1:
        present = present+1
    else:
        absent = absent+1
print("no of stu present:",present)
print("no of stu absent:", absent)

# Find total expense
# Find highest expense day
# Find lowest expense day

exp = [120, 300, 150, 90, 450]
total = sum(exp)
maxi = max(exp)
mini = min(exp)
print(total,maxi,mini)


# PW At least 1 digit
# At least 1 uppercase letter
# output strong or weak

PW = input("Enter password:")

has_upper = False
has_digit = False

for i in range(len(PW)):
    if PW[i].isupper():
        has_upper = True
    if PW[i].isdigit():
        has_digit = True

if has_upper and has_digit:
    print("Strong")
else:
    print("Weak")


# 0 → available
# 1 → booked
# Count available seats
# Book the first available seat

seats = [0, 1, 0, 0, 1]
for i in range(len(seats)):
    if(seats[i]==0):
        seats[i] = 1
print(seats)

# Total credited amount
# Total debited amount
# Final balance

trans = [500, -200, 300, -100, -400]
profit = 0
loss = 0
for i in range(len(trans)):
    if(trans[i] > 1 ):
        profit = profit + trans[i]
    else:
        loss = loss + trans[i]
print(profit)
print(loss)
final_amt = profit + loss
print(final_amt)

#09/01/2026

# Use a while loop
# Keep withdrawing 500
# Print the balance after each withdrawal

balance = 5000
withdraw = 500

while balance > 0:
    balance = balance - withdraw
    print("Remaining balance:", balance)


battery = 100

while battery > 0:
    print("Battery level:", battery, "%")
    battery = battery - 10

import time

battery = 100
hour = 1

while battery > 0:
    print("Hour", hour, "→ Battery level:", battery,"%")
    battery = battery - 10
    hour += 1
    time.sleep(3)   # simulating 1 hour

#FUNCTION BASED PROBLEMS

# Create a function that:
# Takes units consumed as input
# Each unit costs 5
# Returns the total bill amount

def current(a):
    bill = a * 5
    return bill
val = int(input("Enter Your current unit:"))
print("Your Bill Amount:",current(val))


# Takes number of present days
# Total days = 30
# If attendance ≥ 75% → "Allowed"
# Else → "Not Allowed"

total = 30
def attend(b):
    percentage = (b/total) * 100
    return(percentage)
attended = int(input("How may days have you attended:"))
print("Your Attendance Percentage is",attend(attended))

# Balance = 5000
# Ask user to enter withdrawal amount
# Handle:
# Non-numeric input
# Withdrawal more than balance
# Try–except + condition

balance = 5000
try:
    amount = int(input("Enter amount to withdraw:"))
except:
    print("ValueError Non-Numeric Value")
else:
    if(amount > balance):
        print("Insufficient balance")
    else:
        current_bal = balance - amount
        print("Remove Your Card")
        print("Your Current Balance is",current_bal)
