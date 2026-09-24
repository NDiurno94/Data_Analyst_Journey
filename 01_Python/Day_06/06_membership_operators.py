# ============================================================
# MEMBERSHIP OPERATORS - in AND not in
# ============================================================

"""Membership asks whether something is present.
For strings, it checks for a substring and is case-sensitive.
A list is a collection of items inside square brackets.
For a list, membership checks for an equal item."""

skills_text = "Python, SQL and Excel"
print("Python" in skills_text)      # True
print("python" in skills_text)      # False
print("Java" not in skills_text)    # True
print("Py" in skills_text)          # True

skills = ["Python", "SQL", "Excel"]
print("Python" in skills)  # True
print("Py" in skills)      # False; no complete item equals "Py"


