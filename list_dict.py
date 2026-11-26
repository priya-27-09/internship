students = ["Priya", "kaviya", "jeeva"]
print("Students:", students)
print("First student:", students[0])
students.append("Meena")
students.remove("kaviya")
print("Updated list:", students)
for student in students:
    print("Hello", student)
student = {
    "name": "Priya",
    "age": 18,
    "mark": 90
}
print("Name:", student["name"])
print("Mark:", student["mark"])
student["city"] = "Coimbatore"
student["mark"] = 95
print("Updated student:", student)
for key, value in student.items():
    print(key, ":", value)