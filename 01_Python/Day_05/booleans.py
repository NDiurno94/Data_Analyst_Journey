# ============================================================
# BOOLEANS IN PYTHON
# ============================================================

"""A Boolean represents one of only two values:

True
False

The Boolean data type is called bool.

Important: True and False begin with capital letters and are
written without quotation marks.
"""

a = True
b = False

print(a)
print(b)
print(type(a))    # bool
print(type(b))    # bool


# ============================================================
# BOOLEANS ARE NOT STRINGS
# ============================================================

"""True is a Boolean, while "True" is text.
Their values may look similar when printed, but their types are
different."""

c = True
d = "True"

print(c, type(c))    # True <class 'bool'>
print(d, type(d))    # True <class 'str'>


# ============================================================
# COMPARISONS RETURN BOOLEANS
# ============================================================

"""A comparison asks a question about two values.
Python answers that question with True or False.

==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to

Do not confuse = with ==.
= assigns a value to a variable.
== compares two values.
"""

print(10 > 9)       # True
print(10 == 9)      # False
print(10 < 9)       # False
print(10 != 9)      # True
print(10 >= 10)     # True
print(8 <= 10)      # True


# ============================================================
# COMPARING VARIABLES
# ============================================================

e = 32
f = 18

g = e > f
h = e == f

print(g, type(g))   # True, bool
print(h, type(h))   # False, bool


# ============================================================
# COMPARING STRINGS
# ============================================================

"""Strings can also be compared.
Python comparisons are case-sensitive."""

i = "Python"
j = "Python"
k = "python"

print(i == j)       # True
print(i == k)       # False
print(i != k)       # True


# ============================================================
# BOOLEAN RESULTS FROM STRING OPERATIONS
# ============================================================

"""Several string operations and methods learned on Day 4
also return Boolean results."""

l = "I am learning Python"
m = "12345"

print("Python" in l)        # True
print("Java" not in l)      # True
print(l.startswith("I"))    # True
print(l.endswith("SQL"))    # False
print(m.isdigit())           # True


# ============================================================
# THE bool() FUNCTION
# ============================================================

"""bool() evaluates a value and returns True or False."""

print(bool("Hello"))    # True
print(bool(15))         # True
print(bool(3.5))        # True


# ============================================================
# VALUES THAT EVALUATE TO TRUE
# ============================================================

"""Most values evaluate to True.

Examples include:
- non-empty strings
- non-zero numbers
- non-empty collections

Even a string containing "False" or "0" is True because it is
not empty."""

print(bool("abc"))      # True
print(bool("False"))    # True
print(bool("0"))        # True
print(bool(123))        # True
print(bool(-10))        # True
print(bool(["Python"])) # True


# ============================================================
# VALUES THAT EVALUATE TO FALSE
# ============================================================

"""The main falsy values are:

- False
- None
- zero: 0, 0.0 and 0j
- empty strings
- empty collections such as [], (), {} and set()
"""

print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(0.0))    # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(()))     # False
print(bool({}))     # False
print(bool(set()))  # False


# ============================================================
# SPACES ARE CONTENT
# ============================================================

"""A string containing a space is not empty.
It therefore evaluates to True."""

n = ""
o = " "

print(bool(n))      # False
print(bool(o))      # True


# ============================================================
# isinstance() RETURNS A BOOLEAN
# ============================================================

"""isinstance() checks whether a value has a specified type."""

p = 200
q = "200"

print(isinstance(p, int))    # True
print(isinstance(p, str))    # False
print(isinstance(q, str))    # True


# ============================================================
# SAVING BOOLEAN RESULTS
# ============================================================

age = 32
minimum_age = 18
old_enough = age >= minimum_age

language = "Python"
learning_python = language == "Python"

print(f"Old enough: {old_enough}")
print(f"Learning Python: {learning_python}")
