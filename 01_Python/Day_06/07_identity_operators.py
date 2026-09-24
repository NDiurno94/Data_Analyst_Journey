# ============================================================
# IDENTITY OPERATORS - is AND is not
# ============================================================

"""== asks whether values are equal.
is asks whether two names refer to the very same object.

The two list expressions below create separate objects.
Assigning alias = first gives the same object another name.
Use == to compare numbers or text, not is.
Use is None or is not None to check for a missing value."""

first = ["Python", "SQL"]
second = ["Python", "SQL"]
alias = first

print(first == second)      # True
print(first is second)      # False
print(first is alias)       # True
print(first is not second)  # True

result = None
print(result is None)      # True
print(result is not None)  # False


