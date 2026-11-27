try:
    marks = {"Priya": 90}
    name = input("Enter student name: ")
    print(marks[name])
except KeyError:
    print("Student name not found")
except ValueError:
    print("Invalid value")
finally:
    print("Done")