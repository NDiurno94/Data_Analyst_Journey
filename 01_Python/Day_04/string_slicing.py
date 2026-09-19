# ============================================================
# SLICING STRINGS
# ============================================================

"""Slicing returns part of a string.

The basic syntax is:

string[start:end]

The start index is included, but the end index is not included.
"""

a = "Hello, World!"

print(a[2:5])    # llo
print(a[0:5])    # Hello


# ============================================================
# SLICE FROM THE START
# ============================================================

"""Leave out the start index to begin at index 0.
recall that e[start:stop] so START is included, but STOP is excluded"""

b = "Lausanne"

print(b[:4])     # Laus


# ============================================================
# SLICE TO THE END
# ============================================================

"""Leave out the end index to continue to the final character."""

c = "Data Analysis"

print(c[5:])     # Analysis


# ============================================================
# COPY THE WHOLE STRING
# ============================================================

"""Leaving out both indexes returns the complete string."""

d = "Python"

print(d[:])      # Python


# ============================================================
# NEGATIVE SLICING
# ============================================================

""" Character:   H  e  l  l  o  ,     W  o  r  l  d  !
    Positive:    0  1  2  3  4  5  6  7  8  9 10 11 12
    Negative:  -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 """


"""Negative indexes count backwards from the end.
The end index is still excluded."""

e = "Hello, World!"

print(e[-6:-1])  # World
print(e[-6:])    # World!


# ============================================================
# INDEXING COMPARED WITH SLICING
# ============================================================

"""Indexing returns one character.
Slicing returns a range of characters."""

f = "London"

print(f[0])      # L
print(f[0:3])    # Lon
