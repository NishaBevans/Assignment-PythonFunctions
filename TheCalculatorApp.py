#Task 1: Create functions for each arithmetic operation.
import math

def add(num1, num2):
    result = num1 + num2
    print(result)
def subtract(num1, num2):
    result = num1 - num2
    print(result)
def multiply(num1, num2):
    result = num1 * num2
    print(result)
def divide(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except: 
        print("Sorry ! You cant divide by zero! ")

#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

user_input = input("Choose what operation you would like to use: (add/subtract/multiply/divide)")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

if user_input == "add":
    add(num1, num2)
if user_input == "subtract":
    subtract(num1, num2)
if user_input == "multiply":
    multiply(num1, num2)
if user_input == "divide":
    divide(num1, num2)

#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
