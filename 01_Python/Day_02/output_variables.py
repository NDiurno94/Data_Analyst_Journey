# ============================================================
# OUTPUT VARIABLES IN PYTHON
# ============================================================

"""Python uses the print() function to display values on the screen.

You can print text, numbers, variables, or multiple values together."""

name = "Nicola"
age = 32

print(name)
print(age)


# ============================================================
# PRINTING MULTIPLE VARIABLES
# ============================================================

"""You can print multiple variables in the same print() function
by separating them with commas.

Python automatically adds a space between the values."""

first_name = "Nicola"
last_name = "Diurno"

print(first_name, last_name)


# ============================================================
# ADDING NUMBERS
# ============================================================

"""When the + operator is used with numbers, Python performs
mathematical addition."""

x = 10
y = 5

print(x + y)    # Output: 15


# ============================================================
# STRING CONCATENATION
# ============================================================

"""When the + operator is used with strings, Python joins the
strings together.

This is called string concatenation."""

first_name = "Nicola"
last_name = "Diurno"

full_name = first_name + " " + last_name

print(full_name)    # Output: Nicola Diurno


# ============================================================
# NUMBERS AND STRINGS WITH +
# ============================================================

"""The + operator behaves differently depending on the data type.

With numbers, it performs addition.
With strings, it joins the values together."""

number_1 = 10
number_2 = 5

print(number_1 + number_2)    # Output: 15

text_1 = "10"
text_2 = "5"

print(text_1 + text_2)        # Output: 105


# ============================================================
# COMBINING DIFFERENT DATA TYPES
# ============================================================

"""Python cannot directly concatenate a string and an integer
using the + operator.

The number must first be converted to a string using str()."""

name = "Nicola"
age = 32

print(name + " is " + str(age) + " years old.")


# ============================================================
# USING COMMAS WITH DIFFERENT DATA TYPES
# ============================================================

"""Another way to print different data types together is to use
commas inside print().

When commas are used, Python handles the different data types
automatically, so casting is not required."""

name = "Nicola"
age = 32
height = 1.70

print("Name:", name)
print("Age:", age)
print("Height:", height)


# ============================================================
# SUMMARY
# ============================================================

"""In this file you learned how to:

- Display variables using print().
- Print multiple variables together.
- Add numerical values using +.
- Concatenate strings using +.
- Understand the difference between addition and concatenation.
- Convert values using str() when combining different data types.
- Print different data types together using commas."""