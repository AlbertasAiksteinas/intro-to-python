# Video alternative: https://vimeo.com/954334376/0c486313d0#t=625

# Here's a mindbender for you:

a = 10
b = 20
a = b
print(f"a is {a}")
print(f"b is {b}")

# @TASK: What does that output? And why? Take a guess, then
# run the code and see.

# Was it what you expected?

# Try to puzzle it out, and then move on to
# 020_state_tables.py
# Initial variable values
x = 5
y = 15
z = 25
print(f"Initial values: x = {x}, y = {y}, z = {z}")
x = y
print(f"After x = y: x = {x}, y = {y}, z = {z}")
y = z
print(f"After y = z: x = {x}, y = {y}, z = {z}")
z = x + y
print(f"After z = x + y: x = {x}, y = {y}, z = {z}")
x = x + 10
y = y - 5
z = z * 2
print(f"Final values: x = {x}, y = {y}, z = {z}")
