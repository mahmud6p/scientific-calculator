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
