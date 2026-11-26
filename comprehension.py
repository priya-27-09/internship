# LIST COMPREHENSION

numbers = [i for i in range(1, 11)]
print("Numbers:", numbers)
even = [i for i in range(1, 11) if i % 2 == 0]
print("Even Numbers:", even)
odd = [i for i in range(1, 11) if i % 2 != 0]
print("Odd Numbers:", odd)
squares = [i ** 2 for i in range(1, 6)]
print("Squares:", squares)
cubes = [i ** 3 for i in range(1, 6)]
print("Cubes:", cubes)
marks = [90, 35, 80, 25, 70]
passed = [mark for mark in marks if mark >= 40]
print("Passed Marks:", passed)
names = ["priya", "selva", "surekha"]
upper_names = [name.upper() for name in names]
print("Uppercase Names:", upper_names)

# DICTIONARY COMPREHENSION

square_dict = {i: i ** 2 for i in range(1, 6)}
print("Square Dictionary:", square_dict)
cube_dict = {i: i ** 3 for i in range(1, 6)}
print("Cube Dictionary:", cube_dict)
students = ["Priya", "Selva", "Surekha"]
student_marks = [90, 85, 95]
result = {students[i]: student_marks[i] for i in range(3)}
print("Student Marks:", result)
marks_data = {"Priya": 90, "Selva": 35, "Surekha": 95, "Meena": 25}
passed_students = {name: mark for name, mark in marks_data.items() if mark >= 40}
print("Passed Students:", passed_students)
languages = {"language1": "python", "language2": "java", "language3": "html"}
upper_languages = {key: value.upper() for key, value in languages.items()}
print("Uppercase Languages:", upper_languages)