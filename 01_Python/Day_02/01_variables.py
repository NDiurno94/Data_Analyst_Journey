# ============================================================
# CREATING VARIABLES IN PYTHON
# ============================================================

'''A variable is created by assigning a value to it using the
equals sign (=).

For example, to create a variable called "name" and assign
the value "John" to it, you would write:'''

name = "John"
x = 5          # Integer
y = 3.14       # Float
z = True       # Boolean

'''You can display the value stored inside a variable by using
the print() function:'''

print(name)
print(x)
print(y)
print(z)


# ============================================================
# CHANGING THE VALUE OF A VARIABLE
# ============================================================

'''Variables can store different types of values, such as strings,
integers, floating-point numbers and Booleans.

A variable can also be reassigned during the execution of a program.
This means that its value, and even its data type, can change.'''

d = 10         # d is an integer
d = "Hello"    # d is now a string

print(d)       # Output: Hello


# ============================================================
# CASTING VARIABLES IN PYTHON
# ============================================================

'''Casting is the process of converting a value from one data type
to another.

Python provides functions such as str(), int() and float()
to perform these conversions.'''

e = str(3)       # Converts the integer 3 into the string "3"
f = int("3")     # Converts the string "3" into the integer 3
g = float(3)     # Converts the integer 3 into the float 3.0

'''You can use type() to check the data type after casting:'''

print(type(e))   # <class 'str'>
print(type(f))   # <class 'int'>
print(type(g))   # <class 'float'>

'''You can also print the values themselves:'''

print(e)         # Output: 3
print(f)         # Output: 3
print(g)         # Output: 3.0


# ============================================================
# GET THE TYPE OF A VARIABLE IN PYTHON
# ============================================================

'''The type() function can be used to check the data type
of a variable.'''

h = 10
i = "Hello"
j = 3.14
k = True

print(type(h))   # <class 'int'>
print(type(i))   # <class 'str'>
print(type(j))   # <class 'float'>
print(type(k))   # <class 'bool'>


# ============================================================
# CASE-SENSITIVE VARIABLE NAMES
# ============================================================

'''Strings can be written using either single or double quotes.

Variable names are case-sensitive, meaning that "surname" and
"Surname" are treated as two different variables.'''

surname = "Doe"
Surname = "Smith"

print(surname)   # Output: Doe
print(Surname)   # Output: Smith