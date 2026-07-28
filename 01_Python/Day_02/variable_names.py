# ============================================================
# VARIABLE NAMES IN PYTHON
# ============================================================

'''In Python, variable names can contain letters, numbers and
underscores (_).

Variable names can be short, but descriptive names are usually
better because they make the code easier to understand.

Here are some examples of valid variable names:'''

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''These are all valid variable names in Python.
You can print their values using the print() function:'''

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


# ============================================================
# RULES FOR NAMING VARIABLES
# ============================================================

'''There are some important rules to follow when naming variables
in Python:

- A variable name must start with a letter or an underscore (_).
- A variable name cannot start with a number.
- A variable name can only contain letters, numbers and underscores.
- Variable names cannot contain spaces or hyphens.
- Variable names are case-sensitive.'''

# The following examples are INVALID and are kept as comments
# so that they do not stop the program from running.

# 2myvar = "John"    # Invalid: cannot start with a number
# my-var = "John"    # Invalid: cannot contain a hyphen
# my var = "John"    # Invalid: cannot contain a space

'''If these lines were uncommented, Python would raise a
SyntaxError and the program would not run.'''


# ============================================================
# MULTI-WORD VARIABLE NAMES
# ============================================================

'''When a variable name contains multiple words, there are several
ways to format it.

Some common naming styles are:'''

my_variable_name = "John"    # snake_case
myVariableName = "John"      # camelCase
MyVariableName = "John"      # PascalCase
MY_VARIABLE_NAME = "John"    # UPPER_CASE

print(my_variable_name)
print(myVariableName)
print(MyVariableName)
print(MY_VARIABLE_NAME)

'''These are all valid variable names.

In Python, snake_case is the standard naming convention for
regular variables and is the style you will use most often.'''


# ============================================================
# ASSIGN MULTIPLE VALUES TO MULTIPLE VARIABLES
# ============================================================

'''Python allows you to assign multiple values to multiple
variables in a single line.

The number of variables must match the number of values.'''

x, y, z = "Orange", "Banana", "Cherry"

print(x)    # Output: Orange
print(y)    # Output: Banana
print(z)    # Output: Cherry


# ============================================================
# UNPACKING A COLLECTION
# ============================================================

'''If you have a collection of values, Python allows you to
extract those values into separate variables.

This process is called unpacking.

For example, we can create a list of fruits and unpack each
value into a different variable:'''

fruits = ["apple", "banana", "cherry"]

a, b, c = fruits

print(a)    # Output: apple
print(b)    # Output: banana
print(c)    # Output: cherry
