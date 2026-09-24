# ============================================================
# LOGICAL OPERATORS - and, or, not
# ============================================================

"""For Boolean checks:
and: both checks must be True.
or:  at least one check must be True (both can be True).
not: reverses the truth value.

Left    Right   and     or
True    True    True    True
True    False   False   True
False   True    False   True
False   False   False   False
"""

age = 32
currently_studying = True
has_experience = False

eligible = age >= 18 and currently_studying
has_background = currently_studying or has_experience
needs_experience = not has_experience

print(eligible)          # True
print(has_background)    # True
print(needs_experience)  # True


# ============================================================
# SHORT-CIRCUITING AND TRUTHY VALUES
# ============================================================

"""and stops when its left operand is falsy.
or stops when its left operand is truthy.
Otherwise, Python evaluates the right operand.

and and or return one of their operands, which is not always
a Boolean. not always produces a Boolean.
Use comparisons or bool() when you specifically want True/False."""

print("" or "Guest")          # Guest
print("Nicola" or "Guest")    # Nicola
print("Python" and 6)         # 6
print(bool("Python") and 6 > 0)  # True

records = 0
total = 120
has_high_average = records != 0 and total / records > 20
print(has_high_average)  # False; the division is never evaluated


