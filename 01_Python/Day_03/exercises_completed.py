# ============================================================
# DAY 3 - PYTHON DATA TYPES EXERCISES
# ============================================================

"""Complete each exercise using what you learned during Day 3.

Try to complete the exercises without looking at data_types.py,
numbers.py or casting.py.

Run the file after each exercise to check your code."""


# ============================================================
# EXERCISE 1 - IDENTIFYING DATA TYPES
# ============================================================

"""Create four variables containing:

- your name as text
- your age as a whole number
- your height as a decimal number
- whether you are learning Python using True or False

Print each variable separately."""

# Write your code here:

my_name = "Nicola Diurno"
my_age = 32
my_height = 1.70
learning_python = True

print(my_name)
print(my_age)
print(my_height)
print(learning_python)


# ============================================================
# EXERCISE 2 - CHECKING TYPES
# ============================================================

"""Using the four variables from Exercise 1, print the data type
of each variable using type().

Before running the file, try to predict each result."""

# Write your code here:

print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(learning_python))

# ============================================================
# EXERCISE 3 - DIFFERENT BUILT-IN TYPES
# ============================================================

"""Create one variable for each of the following values:

- "Python"
- 25
- 3.14
- 2j
- ["red", "green", "blue"]
- ("London", "Rome", "Geneva")
- {"name": "Nicola", "age": 32}
- {"Python", "SQL", "Excel"}
- False
- None

Print the type of every variable."""

# Write your code here:

a = "Python"
b = 25
c = 2j
d = ["red", "green", "blue"]
e = ("London", "Rome", "Geneva")
f = {
    "name": "Nicola",
    "age": 3
}
g = {"Python","SQL","Excel"}
h = False
i = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))


# ============================================================
# EXERCISE 4 - INTEGER VALUES
# ============================================================

"""Create three integer variables containing:

- a positive integer
- a negative integer
- a very large integer

Print each value and its data type."""

# Write your code here:

positive = 20
negative = -10
large = 300000

print(positive, type(positive))
print(negative, type(negative))
print(large, type(large))

# ============================================================
# EXERCISE 5 - FLOAT VALUES
# ============================================================

"""Create three float variables containing:

- 5.5
- -12.75
- 10.0

Print each value and its data type."""

# Write your code here:

x = 5.5
y = -12.75
z = 10.0

print(x, type(x))
print(y, type(y))
print(z, type(z))

# ============================================================
# EXERCISE 6 - SCIENTIFIC NOTATION
# ============================================================

"""Create three variables using scientific notation:

- 25e3
- 4E2
- -7.5e4

Print each variable.

Then print the data type of each variable."""

# Write your code here:

one = 25e3
two = 4E2
three = -7.5e4

print(one, type(one))
print(two, type(two))
print(three, type(three))

# ============================================================
# EXERCISE 7 - COMPLEX NUMBERS
# ============================================================

"""Create three complex number variables:

- 3j
- 4 + 2j
- -6j

Print each value and its data type."""

# Write your code here:

l = 3j
m = 4 + 2j
n = -6j

print(l, type(l))
print(m, type(m))
print(n, type(n))

# ============================================================
# EXERCISE 8 - CASTING TO INTEGER
# ============================================================

"""Create the following variables:

o = 7.9
p = "15"

Create two NEW variables:

- convert a into an integer
- convert b into an integer

Print the converted values and their data types.

Pay attention to what happens to the decimal part of 7.9."""

o = 7.9
p = "15"

# Write your code here:

o_1 = int(o)
p_1 = int(p)

print(o_1, type(o_1))
print(p_1, type(p_1))

# ============================================================
# EXERCISE 9 - CASTING TO FLOAT
# ============================================================

"""Create the following variables:

c = 8
d = "3.5"

Create two NEW variables:

- convert c into a float
- convert d into a float

Print the converted values and their data types."""

c = 8
d = "3.5"

# Write your code here:



# ============================================================
# EXERCISE 10 - CASTING TO STRING
# ============================================================

"""Create the following variables:

e = 32
f = 1.70

Create two NEW variables by converting e and f into strings.

Print the new values and their data types."""

e = 32
f = 1.70

# Write your code here:



# ============================================================
# EXERCISE 11 - ORIGINAL TYPE VS NEW TYPE
# ============================================================

"""Create a variable containing the string "100".

1. Print its value.
2. Print its data type.
3. Create a NEW variable by converting it to an integer.
4. Print the new value.
5. Print the new data type.

Do not overwrite the original variable."""

# Write your code here:



# ============================================================
# EXERCISE 12 - WHAT WILL HAPPEN?
# ============================================================

"""Study the values below before running your code.

For each value, predict whether it is an int, float, complex,
str, bool or NoneType.

Then use type() to check your predictions."""

g = 50
h = 50.0
i = "50"
j = 5e2
k = 8j
l = True
m = None

# Write your predictions here as comments:
# g:
# h:
# i:
# j:
# k:
# l:
# m:

# Write your type() checks here:



# ============================================================
# EXERCISE 13 - FIX THE CASTING
# ============================================================

"""The variables below contain numbers stored as strings.

Convert them into the correct numeric types:

age should become an integer.
height should become a float.
temperature should become a float.

Print each converted value and its type."""

age = "32"
height = "1.70"
temperature = "-4.5"

# Write your code here:



# ============================================================
# EXERCISE 14 - BUILD A SENTENCE USING CASTING
# ============================================================

"""The variables below have already been created.

Use the + operator and str() to print exactly:

Nicola is 32 years old and is 1.7 metres tall

Do not replace the variables with values directly inside
the sentence."""

first_name = "Nicola"
user_age = 32
user_height = 1.7

# Write your code here:



# ============================================================
# EXERCISE 15 - FINAL DAY 3 CHALLENGE
# ============================================================

"""Create a small Python program that demonstrates what you learned
about data types, numbers and casting.

Requirements:

1. Create variables containing:
   - your name
   - your age
   - your height
   - one integer
   - one float
   - one complex number
   - whether you are learning Python

2. Print the data type of every variable.

3. Create a string containing a number, for example "50".

4. Convert that string into:
   - an integer
   - a float

5. Print both converted values and their data types.

6. Convert your age and height into strings.

7. Use the + operator to build and print a sentence similar to:

   My name is Nicola, I am 32 years old and I am 1.7 metres tall.

8. Use only concepts covered during Day 3.

Try to complete the challenge without looking at the theory files."""

# Write your code here: