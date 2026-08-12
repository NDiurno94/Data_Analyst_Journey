# ============================================================
# BUILT-IN DATA TYPES IN PYTHON
# ============================================================

"""Data types are an important concept in programming.

Variables can store different types of data, and different
data types can be used for different purposes.

Python has several built-in data types, grouped into categories:

Text Type:
- str

Numeric Types:
- int
- float
- complex

Sequence Types:
- list
- tuple
- range

Mapping Type:
- dict

Set Types:
- set
- frozenset

Boolean Type:
- bool

Binary Types:
- bytes
- bytearray
- memoryview

None Type:
- NoneType
"""


# ============================================================
# GETTING THE DATA TYPE
# ============================================================

"""You can use the type() function to check the data type
of a variable."""

x = 5

print(type(x))    # Output: <class 'int'>


# ============================================================
# TEXT TYPE - str
# ============================================================

"""The str data type is used to store text.

Strings are written inside quotation marks."""

y = "Hello World"

print(y)
print(type(y))    # Output: <class 'str'>


# ============================================================
# NUMERIC TYPES
# ============================================================

"""Python has three main numeric data types:

- int
- float
- complex

These will be covered in more detail in the numbers.py file."""

a = 20
b = 20.5
c = 1j

print(type(a))    # int
print(type(b))    # float
print(type(c))    # complex


# ============================================================
# SEQUENCE TYPES
# ============================================================

"""Sequence types are used to store multiple values.

The main sequence types are:

- list
- tuple
- range
"""

d = ["apple", "banana", "cherry"]
e = ("apple", "banana", "cherry")
f = range(6)

print(type(d))    # list
print(type(e))    # tuple
print(type(f))    # range


# ============================================================
# MAPPING TYPE - dict
# ============================================================

"""A dictionary stores information using key-value pairs."""

z = {
    "name": "Nicola",
    "age": 32
}

print(type(z))    # dict


# ============================================================
# SET TYPES
# ============================================================

"""Python has two main set data types:

- set
- frozenset

Sets are used to store collections of unique values."""

g = {"apple", "banana", "cherry"}
h = frozenset({"apple", "banana", "cherry"})

print(type(g))    # set
print(type(h))    # frozenset


# ============================================================
# BOOLEAN TYPE - bool
# ============================================================

"""The bool data type represents one of two values:

True
False
"""

i = True
l = False

print(type(i))    # bool
print(type(l))    # bool


# ============================================================
# BINARY TYPES
# ============================================================

"""Python also includes binary data types.

These are:

- bytes
- bytearray
- memoryview

They are used when working with binary data."""

m = b"Hello"
n = bytearray(5)
o = memoryview(bytes(5))

print(type(m))    # bytes
print(type(n))    # bytearray
print(type(o))    # memoryview


# ============================================================
# NONE TYPE
# ============================================================

"""None represents the absence of a value.

Its data type is NoneType."""

p = None

print(p)
print(type(p))    # NoneType


# ============================================================
# DATA TYPE IS SET AUTOMATICALLY
# ============================================================

"""In Python, the data type is automatically determined
when a value is assigned to a variable.

You do not normally need to declare the data type manually."""

name = "Nicola"
age = 32
height = 1.70
learning_python = True

print(type(name))             # str
print(type(age))              # int
print(type(height))           # float
print(type(learning_python))  # bool


