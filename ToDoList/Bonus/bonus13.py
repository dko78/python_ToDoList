# Define a function named get_age  which:

# (1) has two parameters, year_of_birth and current_year

# (2) the current_year  parameter should be a default parameter

# (3) the default value of current_year should be the current year (e.g., the integer 2025)

# (4) the function should calculate and return the age of the user given the year_of_birth and the current_year.
from datetime import datetime

def get_age(year_of_birth, current_year=datetime.now().year):
    return current_year - year_of_birth


print(get_age(1978))  # Example usage with default current year

# Write a get_nr_items function that:

# (1) gets as a parameter one string with commas (e.g., "john,lisa, teresa")

# (2) the function calculates the number of words (i.e., three words in the above example)

# (3) returns the number of words.

# For example, if I called your function with get_nr_items("john,lisa, teresa") it would return 3.

def get_nr_items(comma_separated_string):
    items = comma_separated_string.split(",")
    return len(items)

print(get_nr_items("john,lisa, teresa"))