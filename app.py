# Python Program Using All Keywords
# Author: Tamad King (a.k.a. You)
# Description: This program demonstrates the use of all Python keywords with user input, connecting all elements logically.

# Importing necessary modules (import, from, as)
from math import sqrt as square_root

# Defining a class (class, def, self)
class Sample:
    def __init__(self, value):
        self.value = value

    def check_value(self):
        if self.value > 0:  # if, elif, else
            return True
        elif self.value == 0:
            return None
        else:
            return False

    def process_value(self):
        try:  # try, except, finally
            result = 10 / self.value
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
        finally:
            print("Process attempted.")
        return result

# Getting user input
user_value = int(input("Enter a number: "))

# Creating instance of Sample
sample_instance = Sample(user_value)

# Using a function with multiple keywords
def analyze_value(value):
    assert isinstance(value, int)  # assert
    print("Analyzing value...")
    
    for i in range(value if value > 0 else 1):  # for, in
        if i == 3:
            break  # break
        print("Step:", i)
    
    while value > 0:  # while
        value -= 1
        if value == 2:
            continue  # continue
        print("Countdown:", value)
    
    return square(value)  # return using lambda

# Lambda function (lambda, return)
square = lambda x: x ** 2

# Demonstrating global, nonlocal, and yield
global_var = 10  # global

def outer():
    nonlocal_var = 5
    def inner():
        nonlocal nonlocal_var  # nonlocal
        nonlocal_var += 1
    inner()
    return nonlocal_var

# Generator function
def generator():
    for num in range(1, 4):
        yield num  # yield

# Boolean values and None (True, False, None)
is_positive = sample_instance.check_value()
print("Is value positive?", is_positive)

# Processing the value
processed_result = sample_instance.process_value()
if processed_result is not None:  # is not
    print("Processed result:", processed_result)
else:
    print("No valid result computed.")

# Testing the generator
gen = generator()
for num in gen:
    print("Generated:", num)

# Testing lambda function
squared_value = analyze_value(user_value)
print("Squared value:", squared_value)

# Using 'is' and 'is not' properly
print("Value is 10:", user_value == 10)  # Fixed SyntaxWarning
print("Value is not 20:", user_value != 20)  # Fixed SyntaxWarning

# Demonstrating 'del'
del squared_value  # Deletes variable reference
print("Squared value deleted.")

# Using 'pass' in an empty function
def placeholder_function():
    pass  # Placeholder for future implementation

# Using 'with' for file handling
with open("output.txt", "w") as file:
    file.write("This file was written using 'with' statement.\n")
    print("File written successfully!")

# Demonstrating 'async' and 'await' (Python async functions)
import asyncio

async def async_function():
    await asyncio.sleep(1)
    print("Async function executed!")

asyncio.run(async_function())
