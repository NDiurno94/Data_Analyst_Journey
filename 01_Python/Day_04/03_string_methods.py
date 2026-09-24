# ============================================================
# MODIFYING STRINGS WITH METHODS
# ============================================================

"""Python provides built-in string methods.

Methods use dot notation:

string.method()

Strings are immutable, so a method returns a new value instead
of changing the original string.
"""


# ============================================================
# CHANGING LETTER CASE
# ============================================================

a = "Hello, World!"

print(a.upper())       # HELLO, WORLD!
print(a.lower())       # hello, world!

b = "python for DATA analysis"

print(b.capitalize())  # Python for data analysis
print(b.title())       # Python For Data Analysis


# ============================================================
# REMOVING OUTER WHITESPACE
# ============================================================

"""strip() removes whitespace from both ends.
lstrip() removes it from the left.
rstrip() removes it from the right.
Spaces inside the text are not removed.
"""

c = "   Python is useful   "

print(c.strip())
print(c.lstrip())
print(c.rstrip())


# ============================================================
# REPLACING TEXT
# ============================================================

"""replace() returns a new string with matching text replaced."""

d = "I am learning Excel"
e = d.replace("Excel", "Python")

print(d)
print(e)


# ============================================================
# SPLITTING TEXT
# ============================================================

"""split() separates a string wherever it finds the chosen
separator. The result is a list."""

f = "Python,SQL,Excel"
g = f.split(",")

print(g)              # ['Python', 'SQL', 'Excel']
print(type(g))         # list


# ============================================================
# FINDING AND COUNTING TEXT
# ============================================================

"""find() returns the index where text first appears.
It returns -1 when the text is not found.

count() returns how many times text appears.
"""

h = "banana"

print(h.find("n"))    # 2
print(h.find("z"))    # -1
print(h.count("a"))   # 3


# ============================================================
# CHECKING STRING CONTENT
# ============================================================

"""These methods return True or False."""

i = "Python"
j = "12345"
k = "Python3"

print(i.startswith("Py"))  # True
print(i.endswith("on"))    # True
print(i.isalpha())          # True
print(j.isdigit())          # True
print(k.isalnum())          # True


# ============================================================
# SAVING A METHOD RESULT
# ============================================================

l = "  nicola diurno  "
m = l.strip().title()

print(l)                    # original value
print(m)                    # Nicola Diurno
