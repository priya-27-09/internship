def add(a: int, b: int) -> int:
    return a + b
def greet(name: str) -> str:
    return "Hello " + name
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)
print(add(10, 20))
print(greet("Priya"))
print(calculate_average([80, 90, 100]))