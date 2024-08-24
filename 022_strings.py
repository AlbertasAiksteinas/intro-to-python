# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=308

# A string is a sequence of characters (letters).

# You've already seen the string syntax dotted around. Here
# it is:

my_name = "Kay"
print(my_name)

# They are surrounded by double quotes:

my_name = "Kay"

# Or single quotes:

my_name = 'Kay'

# In Python, there's no meaningful difference between the
# two.

# Try out creating a string with your name in it:

your_name = "Andrius"
print(your_name)

# @TASK: Check your work by running this file with:
# python 022_strings.py

# As you may have worked out, the `print(string)` function
# prints a string to the shell so you can see it.

# When you're satisfied, move on to 023_string_indexing.py
# Example Python script for string operations

# Define a variable for your name
your_name = "Andrius"  # Replace 'Alice' with your actual name

# Example operations on strings

# Concatenate strings
greeting = "Hello, " + your_name + "!"
print(greeting)

# Get the length of a string
name_length = len(your_name)
print(f"The length of your name is: {name_length}")

# Convert a string to uppercase
upper_name = your_name.upper()
print(f"Your name in uppercase is: {upper_name}")

# Convert a string to lowercase
lower_name = your_name.lower()
print(f"Your name in lowercase is: {lower_name}")

# Find a substring within a string
substring_position = your_name.find("c")
print(f"The position of 'c' in your name is: {substring_position}")

# Replace a part of the string
replaced_name = your_name.replace("Alice", "Bob")
print(f"After replacement: {replaced_name}")

# Split a string into a list
name_parts = your_name.split("c")
print(f"Name split by 'c': {name_parts}")

# Join a list of strings into a single string
joined_name = "-".join(name_parts)
print(f"Joined name with '-': {joined_name}")
