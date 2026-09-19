# ============================================================
# STRINGS IN PYTHON
# ============================================================

"""A string is text surrounded by quotation marks.

Python accepts both single quotes and double quotes.
"""

a = "Hello"
b = 'Python'

print(a)
print(b)
print(type(a))   # str   
print(type(b))   # str


# ============================================================
# QUOTES INSIDE STRINGS
# ============================================================

"""Use one type of quote around a string when the other type
appears inside the text."""

c = "It's a beautiful day"
d = 'He said "Hello"'

print(c)
print(d)


# ============================================================
# MULTILINE STRINGS
# ============================================================

"""Three quotation marks create a string that continues across
more than one line. The line breaks become part of the string."""

e = """Python is readable.
Python is useful.
Python is fun to learn."""

print(e)


# ============================================================
# ACCESSING CHARACTERS
# ============================================================

"""Each character has an index. Indexing begins at 0.

A single character is also a string in Python.
"""

f = "Python"

print(f[0])       # P
print(f[1])       # y
print(f[5])       # n
print(type(f[0])) # str


# ============================================================
# NEGATIVE INDEXING
# ============================================================

"""Negative indexes count backwards from the end.

-1 is the final character, -2 is the second-to-last character,
and so on.
"""

g = "Geneva"

print(g[-1])      # a
print(g[-2])      # v


# ============================================================
# STRING LENGTH
# ============================================================

"""The len() function returns the number of characters.
Spaces and punctuation are included in the count."""

h = "Hello, World!"

print(len(h))     # 13


# ============================================================
# CHECKING A STRING
# ============================================================

"""The in keyword checks whether text is present.
The not in keywords check whether text is absent.
Both expressions produce a Boolean value."""

i = "Python is useful for data analysis"

print("Python" in i)         # True
print("SQL" in i)            # False
print("Java" not in i)       # True


# ============================================================
# STRINGS ARE IMMUTABLE
# ============================================================

"""A string cannot be changed in place after it is created.
String operations and methods return new strings instead."""

j = "hello"
k = j.upper()

print(j)         # hello
print(k)         # HELLO
