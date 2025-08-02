#students = ["Robb", "Jon", "Bran", "Dany"]
#houses = ["Stark", "Stark", "Stark", "Targaryen"]
'''
print(students[0])
print(students[1])
print(students[2])
'''

'''
for student in students:
    print(student)


for i in range(len(students)):
    print(i + 1, students[i])
'''
'''
students = {
    "Robb": "Stark",
    "Jon": "Stark",
    "Bran": "Stark",
    "Dany": "Targaryen"
}
# can use keys as index for dicts
#print(students["Robb"])
#print(students["Jon"])
#print(students["Bran"])
#print(students["Dany"])

for student in students:
    print(student, students[student], sep=", ")
'''

students = [
    {"name": "Robb", "house": "Stark", "patrnous": None},
    {"name": "Jon", "house": "Snow", "patrnous": "Ghost"},
    {"name": "Bran", "house": "Stark", "patrnous": "Summer"},
    {"name": "Dany", "house": "Targaryen", "patrnous": "Drogon"}
]

for student in students:
    print(student["name"], student["house"], student["patrnous"], sep=", ")
