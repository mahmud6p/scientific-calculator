# Scientific Calculator Project
# Author: Prince Mahmud

def main():
    print("Welcome to Scientific Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")

if __name__ == "__main__":
    main()
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to Scientific Calculator")
    choice = int(input("Enter choice (1-Addition, 2-Subtraction): "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def main():
    print("Welcome to Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice: "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
import math

def square_root(x):
    if x < 0:
        return "Error: Negative number"
    return math.sqrt(x)
def power(a, b):
    return math.pow(a, b)
def trig_functions(angle):
    return {
        "sin": math.sin(math.radians(angle)),
        "cos": math.cos(math.radians(angle)),
        "tan": math.tan(math.radians(angle))
    }
def main():
    print("Welcome to Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Trigonometric Functions")

    choice = int(input("Enter choice: "))

    if choice in [1,2,3,4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1: print("Result:", add(a,b))
        elif choice == 2: print("Result:", subtract(a,b))
        elif choice == 3: print("Result:", multiply(a,b))
        elif choice == 4: print("Result:", divide(a,b))
    elif choice == 5:
        x = float(input("Enter number: "))
        print("Result:", square_root(x))
    elif choice == 6:
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", power(a,b))
    elif choice == 7:
        angle = float(input("Enter angle in degrees: "))
        print("Results:", trig_functions(angle))
    else:
        print("Invalid choice")

def logarithm(a, base=10):
    if a <= 0:
        return "Error: Non-positive number"
    return math.log(a, base)
def exponential(a):
    return math.exp(a)
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    return math.factorial(n)
last_result = None

def save_result(value):
    global last_result
    last_result = value
    return "Result saved!"

def recall_result():
    return last_result if last_result is not None else "No result saved yet"
import math

def logarithm(a, base=10):
    if a <= 0:
        return "Error: Non-positive number"
    return math.log(a, base)
def exponential(a):
    return math.exp(a)
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    return math.factorial(n)
last_result = None

def save_result(value):
    global last_result
    last_result = value
    return "Result saved!"

def recall_result():
    return last_result if last_result is not None else "No result saved yet"
