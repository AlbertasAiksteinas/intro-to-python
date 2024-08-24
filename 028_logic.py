from lib.helpers import check_that_these_are_equal

# == Function: a_or_b ==

print("")
print("Function: a_or_b")

def a_or_b(a, b):
    return a or b

check_that_these_are_equal(a_or_b(True, True), True)
check_that_these_are_equal(a_or_b(True, False), True)
check_that_these_are_equal(a_or_b(False, True), True)
check_that_these_are_equal(a_or_b(False, False), False)

# == Exercise One: a_and_b ==

print("")
print("Function: a_and_b")

def a_and_b(a, b):
    # Return True if both a and b are True, else False
    return a and b

check_that_these_are_equal(a_and_b(True, True), True)
check_that_these_are_equal(a_and_b(True, False), False)
check_that_these_are_equal(a_and_b(False, True), False)
check_that_these_are_equal(a_and_b(False, False), False)

# == Exercise Two: not_a ==

print("")
print("Function: not_a")

def not_a(a):
    # Return the opposite Boolean value of a
    return not a

check_that_these_are_equal(not_a(True), False)
check_that_these_are_equal(not_a(False), True)
