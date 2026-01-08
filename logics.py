#1
for i in range(1, 6):
    for j in range(6 - i):
        print(5, end=" ")
    print()

#2
data = [2, 4, 1, 5, 7, 9, 8]
n = len(data)

for i in range(n):
    for j in range(i + 1, n):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
print(data)

5
a = 0
b = 1

print(a)
print(b)

for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c

#4
num = [1,2,3,4,5]

for i in range(len(num)):
    for j in range (i+1,len(num)):
        if (num[i] + num[j] == 6):
            print(f"({num[i]},{num[j]})")

#3
val = [1, 2, 4, 5]
n = 5

for i in range(1, n + 1):
    if i not in val:
        print("Missing value:", i)
        break
#3
given_num = [3, 3, 4, 2, 3, 3, 3]
mid = len(given_num)/2

for i in range(len(given_num)):
    rep = 1
    for j in range(i+1,len(given_num)):
        if (given_num[i] == given_num[j]):
            rep = rep+1
    if(rep > mid):
        print("majority element:",given_num[i])
        break


# 6
N = [1, 2, 3, 4, 5]
K = 2

first_part = []
second_part = []

length = len(N)

for i in range(length):
    if i < length - K:
        first_part.append(N[i])
    else:
        second_part.append(N[i])

rotated = second_part + first_part
print(rotated)

