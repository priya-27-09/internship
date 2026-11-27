import calc
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
def greet():
    print("Welcome to Python AI-ML Internship!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    greet()
    result = add(10, 20)
    print("Addition:", result)