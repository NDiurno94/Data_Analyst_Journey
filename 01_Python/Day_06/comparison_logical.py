"""DAY 5 - COMPARISON AND LOGICAL OPERATORS

Comparison and logical expressions normally produce a Boolean value:
True or False.
"""


# ============================================================
# 1. COMPARISON OPERATORS
# ============================================================

x = 10
y = 6

print(x == y)   # Equal to: False
print(x != y)   # Not equal to: True
print(x > y)    # Greater than: True
print(x < y)    # Less than: False
print(x >= 10)  # Greater than or equal to: True
print(y <= 6)   # Less than or equal to: True


# IMPORTANT:
# = assigns a value.
# == compares two values.

age = 32
print(age == 32)  # True


# Strings can also be compared.

city = "Lausanne"
print(city == "Lausanne")  # True
print(city != "Geneva")    # True


# ============================================================
# 2. LOGICAL OPERATORS
# ============================================================

# and is True only when BOTH conditions are True.

age = 32
has_ticket = True

print(age >= 18 and has_ticket)  # True


# or is True when AT LEAST ONE condition is True.

speaks_italian = True
speaks_french = False

print(speaks_italian or speaks_french)  # True


# not reverses a Boolean value.

is_raining = False

print(not is_raining)  # True


# ============================================================
# 3. COMBINING COMPARISONS
# ============================================================

temperature = 22

print(temperature >= 18 and temperature <= 25)  # True


# Python also permits chained comparisons.

print(18 <= temperature <= 25)  # True


# Parentheses make longer expressions easier to understand.

years_experience = 12
knows_python = True
knows_sql = False

is_suitable = years_experience >= 2 and (knows_python or knows_sql)
print(is_suitable)  # True


# ============================================================
# SUMMARY
# ============================================================

# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# and requires both conditions to be True
# or requires at least one condition to be True
# not reverses True and False

