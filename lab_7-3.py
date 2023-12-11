def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    # Statement to print "Hello World!"
    print("Hello World!")

    # Returning the docstring
    return greeting.__doc__

# Calling the function
greeting()

# Test cases
# Case 1: Calling the function and printing the docstring
print(greeting())

# Case 2: Calling the function multiple times
for _ in range(3):
    greeting()

# Case 3: Storing the docstring in a variable and printing it
docstring_var = greeting.__doc__
print(docstring_var)
