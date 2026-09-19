"""DAY 5 - IDENTITY AND MEMBERSHIP OPERATORS"""


# ============================================================
# 1. IDENTITY OPERATORS
# ============================================================

# is checks whether two variables refer to the SAME object.
# == checks whether two values are EQUAL.

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1

print(list_1 == list_2)  # True: their contents are equal
print(list_1 is list_2)  # False: they are different objects
print(list_1 is list_3)  # True: both names refer to the same object

print(list_1 is not list_2)  # True


# Beginner rule:
# Use == when you want to compare values.
# You will often use is with the special value None later.


# ============================================================
# 2. MEMBERSHIP OPERATORS
# ============================================================

# in checks whether a value exists inside a sequence or collection.

city = "Lausanne"

print("Lau" in city)         # True
print("Geneva" in city)      # False
print("Geneva" not in city)  # True


languages = ["Italian", "English", "French"]

print("English" in languages)      # True
print("German" not in languages)   # True


# Membership tests are case-sensitive.

print("italian" in languages)  # False


# ============================================================
# SUMMARY
# ============================================================

# is      same object
# is not  not the same object
# in      value is present
# not in  value is not present
# ==      equal value

