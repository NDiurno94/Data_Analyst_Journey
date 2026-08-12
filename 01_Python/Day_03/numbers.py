# ============================================================
# NUMBERS IN PYTHON
# ============================================================

"""Python has three main numeric data types:

- int
- float
- complex

A numeric data type is automatically created when a number
is assigned to a variable."""

x = 1       # int
y = 2.8     # float
z = 1j      # complex

print(x)
print(y)
print(z)


# ============================================================
# CHECKING NUMERIC DATA TYPES
# ============================================================

"""The type() function can be used to check which numeric
data type a variable contains."""

x = 1
y = 2.8
z = 1j

print(type(x))    # Output: <class 'int'>
print(type(y))    # Output: <class 'float'>
print(type(z))    # Output: <class 'complex'>


# ============================================================
# INTEGERS - int
# ============================================================

"""An integer, or int, is a whole number without decimals.

Integers can be:

- Positive
- Negative
- Zero

Python integers can also be very large."""

x = 1
y = 35656222554887711
z = -3255522

print(x)
print(y)
print(z)

print(type(x))    # int
print(type(y))    # int
print(type(z))    # int


# ============================================================
# FLOATS - float
# ============================================================

"""A float, or floating-point number, is a number containing
one or more decimal places.

Floats can be positive or negative."""

x = 1.10
y = 1.0
z = -35.59

print(x)
print(y)
print(z)

print(type(x))    # float
print(type(y))    # float
print(type(z))    # float


# ============================================================
# SCIENTIFIC NOTATION
# ============================================================

"""Floats can also be written using scientific notation.

The letter e or E represents a power of 10.

For example:

35e3 means 35 × 10³
12E4 means 12 × 10⁴
"""

x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)

print(type(x))    # float
print(type(y))    # float
print(type(z))    # float


# ============================================================
# COMPLEX NUMBERS - complex
# ============================================================

"""Complex numbers are another numeric data type in Python.

They are written using j to represent the imaginary part
of the number."""

x = 1j
y = 3 + 5j
z = -5j

print(x)
print(y)
print(z)

print(type(x))    # complex
print(type(y))    # complex
print(type(z))    # complex


# ============================================================
# COMPARING NUMERIC TYPES
# ============================================================

"""The value assigned to a variable determines its numeric type.

A whole number is normally an int.
A number with decimals is a float.
A number containing j is a complex number."""

whole_number = 10
decimal_number = 10.5
complex_number = 10j

print(whole_number, type(whole_number))
print(decimal_number, type(decimal_number))
print(complex_number, type(complex_number))