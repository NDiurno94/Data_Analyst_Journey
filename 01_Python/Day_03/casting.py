# ============================================================
# CASTING IN PYTHON
# ============================================================

"""There may be times when you want to specify or change
the data type of a value.

This is called casting.

Python uses constructor functions to perform casting.

The three main constructor functions covered here are:

- int()
- float()
- str()
"""


# ============================================================
# CASTING TO INTEGER - int()
# ============================================================

"""The int() function creates an integer.

It can create an integer from:

- An integer
- A float
- A string containing a whole number

When converting a float to an integer, the decimal part
is removed."""

a = int(1)
b = int(2.8)
c = int("3")

print(a)    # Output: 1
print(b)    # Output: 2
print(c)    # Output: 3

print(type(a))    # int
print(type(b))    # int
print(type(c))    # int


# ============================================================
# FLOAT TO INTEGER
# ============================================================

"""When a float is converted to an integer, Python removes
the decimal part.

It does not round the number."""

d = int(5.9)
e = int(8.2)

print(d)    # Output: 5
print(e)    # Output: 8


# ============================================================
# CASTING TO FLOAT - float()
# ============================================================

"""The float() function creates a floating-point number.

It can create a float from:

- An integer
- A float
- A string containing a valid number
"""

f = float(1)
g = float(2.8)
h = float("3")
i = float("4.2")

print(f)    # Output: 1.0
print(g)    # Output: 2.8
print(h)    # Output: 3.0
print(i)    # Output: 4.2

print(type(f))    # float
print(type(g))    # float
print(type(h))    # float
print(type(i))    # float


# ============================================================
# CASTING TO STRING - str()
# ============================================================

"""The str() function creates a string.

It can convert many different data types into text,
including integers and floats."""

j = str("s1")
k = str(2)
l = str(3.0)

print(j)    # Output: s1
print(k)    # Output: 2
print(l)    # Output: 3.0

print(type(j))    # str
print(type(k))    # str
print(type(l))    # str


# ============================================================
# ORIGINAL TYPE AND NEW TYPE
# ============================================================

"""Casting can be used to create a new value with a
different data type.

The type() function can be used to check both types."""

m = 10
n = float(m)

print(m)
print(type(m))    # int

print(n)
print(type(n))    # float


# ============================================================
# STRING TO NUMBER
# ============================================================

"""A string containing a valid number can be converted
into a numeric data type.

int() can convert a string containing a whole number.
float() can convert a string containing a valid number."""

o = "32"
p = "1.70"

q = int(o)
r = float(p)

print(q)
print(type(q))    # int

print(r)
print(type(r))    # float


# ============================================================
# NUMBER TO STRING
# ============================================================

"""Numbers can be converted into strings using str().

This can be useful when a number needs to be combined
with other text."""

s = 32
t = str(s)

print(t)
print(type(t))    # str