# ============================================================
# STRING CONCATENATION
# ============================================================

"""Concatenation means joining strings.
Use the + operator and add a space string where needed."""

a = "Hello"
b = "World"
c = a + " " + b

print(c)    # Hello World


# ============================================================
# STRINGS AND NUMBERS
# ============================================================

"""The + operator cannot directly join a string and a number.
One solution learned on Day 3 is to convert the number with str()."""

d = "Nicola"
e = 32

print("My name is " + d + " and I am " + str(e) + " years old.")


# ============================================================
# F-STRINGS
# ============================================================

"""An f-string places variables or expressions inside braces.
Write the letter f immediately before the opening quote."""

name = "Nicola"
age = 32
height = 1.70

sentence = f"My name is {name}, I am {age} years old and I am {height} metres tall."

print(sentence)


# ============================================================
# PLACEHOLDERS AND EXPRESSIONS
# ============================================================

"""Anything placed inside the braces is evaluated by Python."""

price = 12
quantity = 3

print(f"The total is {price * quantity} CHF.")


# ============================================================
# FORMAT MODIFIERS
# ============================================================

"""A colon inside a placeholder introduces a format modifier.
.2f displays a number with two digits after the decimal point."""

cost = 9.5

print(f"The coffee costs {cost:.2f} CHF.")


# ============================================================
# ESCAPE CHARACTERS
# ============================================================

"""A backslash introduces an escape character.

Common examples:
\"  double quote
\'  single quote
\\  backslash
\n  new line
\t  tab
"""

print("He said \"Python is useful\".")
print('It\'s time to practise.')
print("C:\\Users\\Nicola")
print("First line\nSecond line")
print("Name:\tNicola")
