def greet():
    print("Welcome to Python Internship!")
greet()
def add(a, b):
    return a + b
result = add(10, 20)
print("Addition:", result)
def calculate_average(marks):
    return sum(marks) / len(marks)
marks = [85, 90, 95, 80]
print("Average:", calculate_average(marks))
def find_marks(marks):
    highest = max(marks)
    lowest = min(marks)
    return highest, lowest
high, low = find_marks(marks)
print("Highest:", high)
print("Lowest:", low)