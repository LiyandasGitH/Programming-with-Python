import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



'''
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
        students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    # lamda "annonymous function" only meant to be used once
    print(f"{student['name']} is from {student['home']}")
'''

'''
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    # lamda "annonymous function" only meant to be used once
    print(f"{student['name']} is from {student['home']}")
'''

'''
students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

#def get_name(student):
#    return student["name"]
    # effect achieved by lambda


for student in sorted(students, key=lambda student: student["name"]):
    # lamda "annonymous function" only meant to be used once
    print(f"{student['name']} is from {student['home']}")
'''


'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''

'''
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

'''

