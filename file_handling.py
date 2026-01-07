
f = open("d2.txt","w")
f.write("Internship day 2. learning about file handling")
f.write("\nChecking whether write will append or overwrite")

f = open("d2.txt", "r+")
f.seek(0,2)
f.write("\nChecking r+ mode, here the content will overwrite if no seek value is given and to read also seek is important\n")
f.seek(0)
fr = f.read()
print(fr)

with open("d2.txt", "a+") as f:
    for i in range(1):
        appen = input("what have you learned:")
        f.write(appen)
        f.seek(0)
        fr=f.read()
        print(fr)


import csv
with open("data.csv", "w") as f:
    fw = csv.writer(f)
    fw.writerow(["name","age"])
    fw.writerow(["hey",23])
    fw.writerow(["hii",22])

with open("data.csv","r") as f:
    fw = csv.reader(f)
    for i in fw:
        print(i)

import json
data = [{"name":"heiley","age":21},{"name":"brener","age":24}]
with open("data.json" , "w") as f:
     json.dump(data,f)

with open("data.json","r") as f:
     fr = json.load(f)
     for a in fr:
          print(a["name"])


import json

data = {"name": "Ramya", "age": 22}
with open("data.json", "w") as f:
    json.dump(data, f)


with open("data.json", "r") as f:
    data = json.load(f)
print(data["name"])
