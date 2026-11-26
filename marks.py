
def analyze_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return average, highest, lowest
marks = [90, 85, 75, 95, 80]
average, highest, lowest = analyze_marks(marks)
print("Student Marks:", marks)
print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
