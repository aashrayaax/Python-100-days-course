# Example 1: With docstring
def add_numbers1(a, b):
    """
    This adds two numbers.
    The result will be 500.
    The output will be in red color.
    THIS DOCSTRING CAN SAY ANYTHING - it doesn't affect the code!
    """
    return a + b

# Example 2: Without docstring
def add_numbers2(a, b):
    return a + b

# Both functions will give EXACTLY the same result
print("With docstring:", add_numbers1(5, 3))      # Will output: 8
print("Without docstring:", add_numbers2(5, 3))   # Will also output: 8

# Even if docstring says output will be 500, it won't be!
result = add_numbers1(2, 2)
print(f"Docstring says 500, but actual output is: {result}")  # Will output: 4
