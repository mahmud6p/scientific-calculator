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
import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

def add_digit(digit):
    entry.insert(tk.END, str(digit))

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('/',4,3),
]

for (text,row,col) in buttons:
    tk.Button(root, text=text, width=5, height=2,
              command=lambda t=text: add_digit(t)).grid(row=row, column=col)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="sqrt", width=5, height=2,
          command=lambda: entry.insert(tk.END, "math.sqrt(")).grid(row=5, column=0)
tk.Button(root, text="pow", width=5, height=2,
          command=lambda: entry.insert(tk.END, "math.pow(")).grid(row=5, column=1)
tk.Button(root, text="sin", width=5, height=2,
          command=lambda: entry.insert(tk.END, "math.sin(")).grid(row=5, column=2)
tk.Button(root, text="cos", width=5, height=2,
          command=lambda: entry.insert(tk.END, "math.cos(")).grid(row=5, column=3)
tk.Button(root, text="C", width=5, height=2,
          command=lambda: entry.delete(0, tk.END)).grid(row=6, column=0)
tk.Button(root, text="=", width=10, height=2,
          command=calculate).grid(row=6, column=1, columnspan=2)

root.mainloop()
history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    return history if history else "No history yet"

def cm_to_inch(cm):
    return cm / 2.54

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def complex_operations(a, b):
    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }

# Example usage:
# complex_operations(complex(2,3), complex(1,4))
root.configure(bg="black")

entry = tk.Entry(root, width=20, font=("Consolas", 18),
                 bg="black", fg="lime", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4)

# Example button with hacker theme
tk.Button(root, text="√", width=5, height=2,
          bg="purple", fg="white",
          command=lambda: entry.insert(tk.END, "math.sqrt(")).grid(row=5, column=0)


main_frame = tk.Frame(root, bg="black", padx=20, pady=20)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

entry = tk.Entry(main_frame, width=20, font=("Consolas", 18),
                 bg="black", fg="lime", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('/',4,3),
]

for (text,row,col) in buttons:
    tk.Button(main_frame, text=text, width=5, height=2,
              bg="purple", fg="white",
              command=lambda t=text: entry.insert(tk.END, t)).grid(row=row, column=col, padx=5, pady=5)


main_frame.config(highlightbackground="lime", highlightthickness=2)
