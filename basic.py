a = [5,10,15,20,25,30,35,40]
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])
print("a[5:] = ", a[5:])
print(a[3])
a[7] = 45
print(a)

Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)


n = int(input("Enter n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1 # update counter
print("The sum is", sum)
