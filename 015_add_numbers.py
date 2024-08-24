from lib.helpers import check_that_these_are_equal

# Video alternative: https://vimeo.com/954334235/902b0b036d#t=444

# @TASK: Now you try. Here's an exercise for you:
#
# Write a function called `add_numbers` that:
#
# * Takes two numbers as input
# * Adds them together
# * Returns the result

# YOUR FUNCTION GOES BELOW THIS LINE

# Function to add two numbers
def add_numbers(num_a, num_b):
    return num_a + num_b

# Function to check if two values are equal
def check_that_these_are_equal(value, expected):
    if value == expected:
        print(f"Test passed: {value} equals {expected}")
    else:
        print(f"Test failed: {value} does not equal {expected}")

# Test the add_numbers function
print("add_numbers(2, 3) is:")
check_that_these_are_equal(
    add_numbers(2, 3),
    5
)

print("add_numbers(3, 5) is:")
check_that_these_are_equal(
    add_numbers(3, 5),
    8
)


# YOUR FUNCTION GOES ABOVE THIS LINE

# @TASK: Check your work by running:

#   python 015_add_numbers.py

# Below is a test for your function.


# When you're done, move on to 016_operators.py
