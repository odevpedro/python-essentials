# This is a comment. Anything on a line after a "#" symbol is ignored by the interpreter.

# Variables can be declared and assigned values using the "=" operator.
# The type of the variable is determined by the value it is assigned.
my_string = "Hello, world!"  # This is a string.
my_int = 42  # This is an integer.
my_float = 3.14  # This is a float (a decimal number).
my_bool = True  # This is a boolean value (True or False).

# We can perform basic arithmetic operations on numbers.
result = 3 + 4  # Addition
result = 4 - 3  # Subtraction
result = 3 * 4  # Multiplication
result = 4 / 3  # Division
result = 4 % 3  # Modulus (remainder of division)

# We can use the "print()" function to output text to the console.
print(my_string)
print(my_int)
print(my_float)
print(my_bool)

# We can use the "input()" function to get input from the user.
name = input("What is your name? ")
print(f"Hello, {name}!")  # The "f" in front of the string indicates that it is a formatted string.

# We can use "if" statements to control the flow of our code based on a condition.
if my_int > 10:
  print("The integer is greater than 10.")
else:
  print("The integer is not greater than 10.")

# We can use "for" loops to repeat a block of code for a given number of iterations.
for i in range(5):  # The "range()" function generates a sequence of numbers from 0 to 4.
  print(i)

# We can use "while" loops to repeat a block of code until a certain condition is met.
count = 0
while count < 5:
  print(count)
  count += 1  # The "count += 1" syntax is shorthand for "count = count + 1".
  #d
