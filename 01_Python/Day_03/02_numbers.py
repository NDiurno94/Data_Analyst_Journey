# ============================================================
# NUMBERS IN PYTHON
# ============================================================

"""Python has three main numeric data types:

- int
- float
- complex

A numeric data type is automatically created when a number
is assigned to a variable."""

a = 1       # int
b = 2.8     # float
c = 1j      # complex

print(a)
print(b)
print(c)


# ============================================================
# CHECKING NUMERIC DATA TYPES
# ============================================================

"""The type() function can be used to check which numeric
data type a variable contains."""

d = 1
e = 2.8
f = 1j

print(type(d))    # Output: <class 'int'>
print(type(e))    # Output: <class 'float'>
print(type(f))    # Output: <class 'complex'>


# ============================================================
# INTEGERS - int
# ============================================================

"""An integer, or int, is a whole number without decimals.

Integers can be:

- Positive
- Negative
- Zero

Python integers can also be very large."""

g = 1
h = 35656222554887711
i = -3255522

print(g)
print(h)
print(i)

print(type(g))    # int
print(type(h))    # int
print(type(i))    # int


# ============================================================
# FLOATS - float
# ============================================================

"""A float, or floating-point number, is a number containing
one or more decimal places.

Floats can be positive or negative."""

l = 1.10
m = 1.0
n = -35.59

print(l)
print(m)
print(n)

print(type(l))    # float
print(type(m))    # float
print(type(n))    # float


# ============================================================
# SCIENTIFIC NOTATION
# ============================================================

"""Floats can also be written using scientific notation.

The letter e or E represents a power of 10.

For example:

35e3 means 35 × 10³
12E4 means 12 × 10⁴
"""

o = 35e3
p = 12E4
q = -87.7e100

print(o)
print(p)
print(q)

print(type(o))    # float
print(type(p))    # float
print(type(q))    # float


# ============================================================
# COMPLEX NUMBERS - complex
# ============================================================

"""Complex numbers are another numeric data type in Python.

They are written using j to represent the imaginary part
of the number."""

r = 1j
s = 3 + 5j
t = -5j

print(r)
print(s)
print(t)

print(type(r))    # complex
print(type(s))    # complex
print(type(t))    # complex


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