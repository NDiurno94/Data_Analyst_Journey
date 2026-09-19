"""DAY 5 - ARITHMETIC AND ASSIGNMENT OPERATORS

Operators perform operations on values and variables.
Run this file, study the outputs, and then change the values.
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

x = 17
y = 5

print("Addition:", x + y)          # 22
print("Subtraction:", x - y)       # 12
print("Multiplication:", x * y)    # 85
print("Division:", x / y)          # 3.4
print("Floor division:", x // y)   # 3
print("Remainder:", x % y)         # 2
print("Exponentiation:", x ** 2)   # 289


# Division with / always produces a float.

print(10 / 2)       # 5.0
print(type(10 / 2)) # <class 'float'>


# Floor division // rounds DOWN to the nearest whole number.

print(17 // 5)      # 3
print(3 // 2)       # 1


# The modulus operator % gives the remainder.
# 17 divided by 5 is 3 with a remainder of 2.

print(17 % 5)       # 2


# Exponentiation ** raises a number to a power.

print(2 ** 3)       # 8: 2 × 2 × 2


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================

# The = operator assigns a value to a variable.

score = 10
print(score)


# These two statements have the same effect.

score = score + 5
print(score)        # 15

score += 5
print(score)        # 20


# Other compound assignment operators work in the same way.

number = 20

number -= 3         # number = number - 3
print(number)       # 17

number *= 2         # number = number * 2
print(number)       # 34

number /= 4         # number = number / 4
print(number)       # 8.5

number //= 2        # number = number // 2
print(number)       # 4.0

number **= 2        # number = number ** 2
print(number)       # 16.0

number %= 6         # number = number % 6
print(number)       # 4.0


# ============================================================
# SUMMARY
# ============================================================

# +   addition
# -   subtraction
# *   multiplication
# /   division
# //  floor division
# %   remainder
# **  exponentiation
# =   assignment
# +=, -=, *=, /= and similar operators update a variable

