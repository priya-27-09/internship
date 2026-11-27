import csv
students = [
    ["Name", "Age", "Marks"],
    ["Priya", 18, 90],
    ["Selva", 19, 85],
    ["Surekha", 18, 95]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)