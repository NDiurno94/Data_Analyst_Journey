# ============================================================
# DAY 6 - PYTHON OPERATORS EXERCISES
# ============================================================

"""Complete one exercise at a time. 
Use the topic files for hints when needed.
Exercises 1-14 are core practice; 15 optional extensions."""


# ============================================================
# EXERCISE 1 - ARITHMETIC WARM-UP
# ============================================================

"""Using a = 19 and b = 4, print their sum, difference, product,
quotient, floor quotient and remainder. Also print a squared."""

a = 19
b = 4

# Write your code here:

print(f"Sum: {a + b} \n"               # 23
      f"Difference: {a - b} \n"        # 15
      f"Product: {a * b} \n"           # 76
      f"Quotient: {a / b} \n"          # 4.75
      f"Floor Quotient: {a // b} \n"   # 4
      f"Reminder: {a % b} \n"          # 3
      f"Squared: {a ** b}")            # 130321


# ============================================================
# EXERCISE 2 - PACKING BOXES
# ============================================================

"""You have 38 items. Each box holds 8 items.
Save and print the number of full boxes and leftover items
using descriptive f-strings."""

items = 38
box_size = 8

# Write your code here:

full_boxes = 38 // 8
leftover_items = 38 % 8

print(f"Full Boxes = {full_boxes} \n"           # 4
      f"Leftover Items = {leftover_items}")     # 6


# ============================================================
# EXERCISE 3 - EVEN OR ODD?
# ============================================================

"""Check whether each number is even using % and ==.
Save each Boolean result and print it."""

first_number = 26
second_number = 31

# Write your code here:

first_is_even = first_number % 2 == 0
second_is_even = second_number % 2 == 0

print(f"first_number is even: {first_is_even}")    # True
print(f"second_number is even: {second_is_even}")  # False

# ============================================================
# EXERCISE 4 - UPDATE A BALANCE
# ============================================================

"""Start with the balance below. Add 40, subtract 25, then
multiply the result by 2 using assignment shortcuts. Print
after each update. Finally divide by 5 with /= and print again."""

# Write your code here:

balance = 100
balance += 40
print(balance)    # 140

balance -= 25
print(balance)    # 115

balance *= 2
print(balance)    # 230

balance /= 5
print(balance)    # 46.0

# ============================================================
# EXERCISE 5 - MORE ASSIGNMENT SHORTCUTS
# ============================================================

"""Starting with number = 29, use //= 4, then **= 2, then %= 6.
Print the value after every update."""

number = 29

# Write your code here:

number //= 4
print(number)     # 7

number **= 2
print(number)     # 49

number %= 6
print(number)     # 1

# ============================================================
# EXERCISE 6 - COMPARE RESULTS
# ============================================================

"""Print whether actual equals target, differs from target,
is greater, is smaller, is at least target and is at most
target. Explain why equality matters for >= and <=."""

actual = 250
target = 250

# Write your code here:
print(actual == target)  # Equals: True
print(actual != target)  # Differs: False
print(actual > target)   # Greater: False
print(actual < target)   # Smaller: False
print(actual >= target)  # At least: True
print(actual <= target)  # At most: True

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

# Write your code here:

student = age >= 18 and currently_studying
print(student)    # True

eligible = currently_studying or has_experience
print(eligible)   # True

no_experience = not has_experience
print(no_experience)    # True


# ============================================================
# EXERCISE 8 - CHECK A RANGE
# ============================================================

"""Save and print whether score is between 60 and 100 inclusive.
Write one version using and and another using a chained
comparison. Then try score = 100 and score = 101."""

# Write your code here:

score = 75
score_in_range = 60 <= score <= 100
print(score_in_range)      # True

score_in_range_2 = 60 <= score and score <= 100
print(score_in_range_2)    # True

score_1 = 100
score_in_range = 60 <= score_1 <= 100
print(score_in_range)      # True

score_in_range_2 = 60 <= score_1 and score_1 <= 100
print(score_in_range_2)    # True

score_2 = 101
score_in_range = 60 <= score_2 <= 100
print(score_in_range)      # False

score_in_range_2 = 60 <= score_2 and score_2 <= 100
print(score_in_range_2)    # False

# ============================================================
# EXERCISE 9 - CHECK MEMBERSHIP
# ============================================================

"""Print whether "Python" and "python" are in skills_text,
whether "Java" is absent, and whether "Py" is in skills_text
and in skills. Explain the last two results."""

skills_text = "Python, SQL and Excel"     # String
skills = ["Python", "SQL", "Excel"]       # List

# Write your code here:
print(f"Python is in the skills text: {"Python" in skills_text} \n"                           # True
      f"python is in the skills text: {"python" in skills_text} \n"                           # False
      f"Java is not in the skills text: {"Java" not in skills_text} \n"                       # True
      f"Py is in skills text: {"Py" in skills_text}, and in skills {"Py" in skills}")         # True False


"""String membership checks for a substring: "Py" appears within "Python", so it’s True.
   List membership checks for a complete matching element: the list contains "Python", but no "Py" element, so it’s False."""

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

# Write your code here:

print(first == second)        # True
print(first is second)        # False
print(first is alias)         # True
print(first is not second)    # True
print(result is None)         # True

"""first is equal to second but is not second. They are different variables and thats why we obtain false output"""


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

# Write your code here:

print(6 + 4 * 3)        # 18
print((6 + 4) * 3)      # 30
print(20 - 8 - 2)       # 10
print(2 ** 2 ** 3)      # 256   Exponentiation (**) groups from right to left, so Python evaluates it as: 2 ** (2 ** 3)
print(True or False and False)        # True    and has higher precedence than or -  True or False → True
print((True or False) and False)      # False   True and False → False


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

# Write your code here:
print(age == 32)     # True
print(5 ** 2)        # 25
print(f"Age: {age}") # Age: 32
print(18 <= age < 65)   # True

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

name = username or "Guest"
print(name)       # Guest  

Check = records != 0 and total / records > 10
print(Check)  # False - and short-circuits: when records != 0 is False, Python skips total / records > 10. This prevents division by zero.

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

# Write your code here:

revenue = units_sold * unit_price                                 # 630 CHF
total_cost = units_sold * cost_per_unit                           # 385 CHF
profit = revenue - total_cost                                     # 245 CHF
average_revenue_per_order = revenue / orders                      # 90.00 CHF
target_reached = revenue >= target                                # True
profitable_and_target_reached = profit > 0 and target_reached     # True
region_matches = region == "Lausanne" or region == "Geneva"       # True
python_present = "Python" in skills                               # True

print(f"Revenue: {revenue:.2f} CHF")
print(f"Total cost: {total_cost:.2f} CHF")
print(f"Profit: {profit:.2f} CHF")
print(f"Average revenue per order: {average_revenue_per_order:.2f} CHF")
print(f"Revenue reaches the target: {target_reached}")
print(f"Profit is positive and target reached: {profitable_and_target_reached}")
print(f"Region is Lausanne or Geneva: {region_matches}")
print(f"Python is present in skills: {python_present}")

# ============================================================
# EXERCISE 15 - OPTIONAL - NEGATIVE FLOOR DIVISION
# ============================================================

"""Predict and print -19 // 4 and -19 % 4.
Check that quotient * 4 + remainder reconstructs -19.
Also compare -4 ** 2 with (-4) ** 2."""

x = -19
y = 4

print(x // y)
print(x % y)

quotient = x // y
remainder = x % y

check = quotient * 4 + remainder == -19
print(f"quotient * 4 + remainder is -19: {check}")



check_1 = -4 ** 2 == (-4) ** 2
print(check_1)
print(f"-4 ^ 2= {-4 ** 2}")
print(f"(-4) ^ 2= {(-4) ** 2}")

