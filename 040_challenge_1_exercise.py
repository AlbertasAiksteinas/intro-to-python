"""# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  pass

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
"""
from lib.helpers import check_that_these_are_equal

def report_long_words(words):
    # Step 1: Filter words longer than 10 characters and without hyphens
    filtered_words = [word for word in words if len(word) > 10 and '-' not in word]
    
    # Step 2: Shorten words longer than 15 characters
    shortened_words = [
        word if len(word) <= 15 else word[:15] + '...' 
        for word in filtered_words
    ]
    
    # Step 3: Format the output string
    if shortened_words:
        result = "These words are quite long: " + ", ".join(shortened_words)
    else:
        result = "These words are quite long: "
    
    return result

# Tests
check_that_these_are_equal(
    report_long_words([
        'hello',
        'nonbiological',
        'Kay',
        'this-is-a-long-word',
        'antidisestablishmentarianism'
    ]),
    "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
    report_long_words([
        'cat',
        'dog',
        'rhinosaurus',
        'rhinosaurus-rex',
        'frog'
    ]),
    "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
    report_long_words([
        'cat'
    ]),
    "These words are quite long: "
)
