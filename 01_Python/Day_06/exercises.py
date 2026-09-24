# ============================================================
# DAY 6 - PYTHON OPERATORS EXERCISES
# ============================================================

"""Complete one exercise at a time. Predict results before running.
Use the topic files for hints when needed.
Exercises 1-14 are core practice; 15-16 are optional extensions."""


# ============================================================
# EXERCISE 1 - ARITHMETIC WARM-UP
# ============================================================

"""Using a = 19 and b = 4, print their sum, difference, product,
quotient, floor quotient and remainder. Also print a squared.
Predict all seven results first."""

a = 19
b = 4

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 2 - PACKING BOXES
# ============================================================

"""You have 38 items. Each box holds 8 items.
Save and print the number of full boxes and leftover items
using descriptive f-strings."""

items = 38
box_size = 8

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 3 - EVEN OR ODD?
# ============================================================

"""Check whether each number is even using % and ==.
Save each Boolean result and print it."""

first_number = 26
second_number = 31

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 4 - UPDATE A BALANCE
# ============================================================

"""Start with the balance below. Add 40, subtract 25, then
multiply the result by 2 using assignment shortcuts. Print
after each update. Finally divide by 5 with /= and print again."""

balance = 100

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 5 - MORE ASSIGNMENT SHORTCUTS
# ============================================================

"""Starting with number = 29, use //= 4, then **= 2, then %= 6.
Predict and print the value after every update."""

number = 29

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 6 - COMPARE RESULTS
# ============================================================

"""Print whether actual equals target, differs from target,
is greater, is smaller, is at least target and is at most
target. Explain why equality matters for >= and <=."""

actual = 250
target = 250

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 7 - COMBINE BOOLEAN CHECKS
# ============================================================

"""Save and print these checks:
- age is at least 18 AND currently_studying is True
- currently_studying OR has_experience is True
- has_experience is NOT True
Use and, or and not with the supplied Boolean variables."""

age = 32
currently_studying = True
has_experience = False

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 8 - CHECK A RANGE
# ============================================================

"""Save and print whether score is between 60 and 100 inclusive.
Write one version using and and another using a chained
comparison. Then try score = 100 and score = 101."""

score = 75

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 9 - CHECK MEMBERSHIP
# ============================================================

"""Print whether "Python" and "python" are in skills_text,
whether "Java" is absent, and whether "Py" is in skills_text
and in skills. Explain the last two results."""

skills_text = "Python, SQL and Excel"
skills = ["Python", "SQL", "Excel"]

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 10 - EQUALITY OR IDENTITY?
# ============================================================

"""Predict and print first == second, first is second,
first is alias, first is not second and result is None.
Explain why equal lists need not be the same object."""

first = ["Excel", "SQL"]
second = ["Excel", "SQL"]
alias = first
result = None

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 11 - PREDICT THE ORDER
# ============================================================

"""Predict and print these expressions:
- 6 + 4 * 3
- (6 + 4) * 3
- 20 - 8 - 2
- 2 ** 2 ** 3
- True or False and False
- (True or False) and False
Explain which operation is grouped first in each case."""

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 12 - FIND AND FIX THE MISTAKES
# ============================================================

"""The commented lines below contain mistakes. Write corrected
versions that check equality, calculate a square and build a
label. Also correct the range check so both comparisons
actually test age."""

age = 32
# print(age = 32)
# print(5 ^ 2)  # Intended: five squared
# print("Age: " + age)
# print(age >= 18 and 65)  # Intended: 18 <= age < 65

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 13 - TRUTHY VALUES AND SAFE DIVISION
# ============================================================

"""Use or to choose "Guest" when username is empty.
Then save a check that records is nonzero AND total / records
is greater than 10. Print both results. Explain why the
division does not cause an error with records = 0."""

username = ""
records = 0
total = 90

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 14 - FINAL DAY 6 CHALLENGE - SALES REPORT
# ============================================================

"""Create a sales report using the supplied data.

1. Calculate revenue, total cost and profit.
2. Calculate average revenue per order (orders is nonzero here).
3. Check whether revenue is at least target.
4. Check whether profit is positive AND the target is reached.
5. Check whether region equals "Lausanne" OR "Geneva".
   Compare region explicitly on both sides of or.
6. Check whether "Python" is present in skills.
7. Save every result in a descriptive variable.
8. Print all results using labelled f-strings. Display monetary
   values with two decimal places using :.2f.

Use only variables, operators and print(). No if statements,
loops or functions are needed."""

units_sold = 35
unit_price = 18
cost_per_unit = 11
orders = 7
target = 600
region = "Lausanne"
skills = "Python, SQL and Excel"

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 15 - OPTIONAL - NEGATIVE FLOOR DIVISION
# ============================================================

"""Predict and print -19 // 4 and -19 % 4.
Check that quotient * 4 + remainder reconstructs -19.
Also compare -4 ** 2 with (-4) ** 2."""

# Write your predictions as comments:

# Write your code here:


# ============================================================
# EXERCISE 16 - OPTIONAL - BITWISE PRACTICE
# ============================================================

"""Using a = 5 (0101) and b = 3 (0011), predict and print
a & b, a | b, a ^ b, ~a, a << 1 and a >> 1.
Explain why ^ does not calculate a power."""

a = 5
b = 3

# Write your predictions as comments:

# Write your code here:


