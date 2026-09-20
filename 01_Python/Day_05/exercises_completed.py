# ============================================================
# DAY 5 - PYTHON BOOLEANS EXERCISES
# ============================================================

"""Complete each exercise using what you learned during Day 5.

Try not to look at booleans.py. Predict the result before you
run each section.
"""


# ============================================================
# EXERCISE 1 - CREATE BOOLEAN VALUES
# ============================================================

"""Create two variables:

- learning_python containing True
- finished_course containing False

Print both values and their data types."""

# Write your code here:

learning_python = True
finished_course = False

print(learning_python, type(learning_python),
      "\n", finished_course, type(finished_course)) # will print the False statement below the True, but one space ahead

print(f"{learning_python}, {type(learning_python)} \n"
      f"{finished_course}, {type(finished_course)}") # but this will actually print both statements one below the other one

# ============================================================
# EXERCISE 2 - BOOLEAN OR STRING?
# ============================================================

"""Create one Boolean True and one string containing "True".
Print each value and its type.

Before running the code, predict whether their types match."""

# Write your prediction as a comment:

# True 'bool'
# True 'string'

# Write your code here:

a = True
b = "True"

print(a, type(a))
print(b, type(b))

print(f"The first {a} is a {type(a)}, \n"
      f"however, the second {b}, is not a boolean but {type(b)} instead.")

# ============================================================
# EXERCISE 3 - PREDICT COMPARISONS
# ============================================================

"""Predict the result of every comparison, then print each one
to check your answers."""

c = 10 > 5
d = 10 < 5
e = 10 == 10
f = 10 != 10
g = 7 >= 7
h = 6 <= 4

# Write your predictions as comments:
# c: True
# d: False
# e: True
# f: False
# g: True
# h: False

# Print the variables here:
print(f"{c} \n"
      f"{d} \n"
      f"{e} \n"
      f"{f} \n"
      f"{g} \n"
      f"{h}")

print(c,d,e,f,g,h)


# ============================================================
# EXERCISE 4 - COMPARE VARIABLES
# ============================================================

"""Use the variables below to check whether:

- age is greater than minimum_age
- age is equal to minimum_age
- age is not equal to minimum_age

Print all three results."""

age = 32
minimum_age = 18

# Write your code here:
print(f"Is age greater than minimum age? {age > minimum_age} \n"
      f"Is age equal to minimum age? {age == minimum_age} \n"
      f"Is age not equal to minimum age? {age != minimum_age}")

# ============================================================
# EXERCISE 5 - COMPARE STRINGS
# ============================================================

"""Compare the strings below and print the results of:

- first_language == second_language
- first_language == third_language
- first_language != third_language

Notice the capital letter."""

first_language = "Python"
second_language = "Python"
third_language = "python"

# Write your code here:
print(f"Is the first language equal to the second? {first_language == second_language} \n"
      f"Is the first language equal to the third? {first_language == third_language} \n"
      f"Is the first languane not equal to the third? {first_language != third_language}")


# ============================================================
# EXERCISE 6 - STRINGS RETURN BOOLEANS
# ============================================================

"""Use Day 4 concepts to check whether:

- "Python" is present in the sentence
- "Java" is absent from the sentence
- the sentence starts with "I"
- the sentence ends with "SQL"

Print every Boolean result."""

sentence = "I am learning Python"

# Write your code here:
print(f"The word Python is present in sentence > {"Python" in sentence} \n"
      f"The word Java is not present in sentence > {"Java" not in sentence} \n"
      f"The sentece starts with the letter I > {sentence.startswith("I")} \n"
      f"The sentence ends with SQL > {sentence.endswith("SQL")}")


# ============================================================
# EXERCISE 7 - EVALUATE TRUE VALUES
# ============================================================

"""Use bool() to evaluate each value below.
Predict the result before running the code."""

i = "Nicola"
l = 32
m = -5
n = ["Python", "SQL"]

# Write your predictions as comments:
# i: True
# l: True
# m: True 
# n: True

# Write your bool() checks here:
print(bool(i))
print(bool(l))
print(bool(m))
print(bool(n))



# ============================================================
# EXERCISE 8 - EVALUATE FALSE VALUES
# ============================================================

"""Use bool() to evaluate each value below.
Print every result."""

o = ""
p = 0
q = 0.0
r = None
s = []

# Write your code here:
print(bool(o))
print(bool(p))
print(bool(q))
print(bool(r))
print(bool(s))


# ============================================================
# EXERCISE 9 - EMPTY STRING OR SPACE?
# ============================================================

"""Use bool() on both variables.
Predict why their Boolean results are different."""

t = ""
u = " "

# Write your prediction as a comment:
'''t results in false as it is an empty string,
however, u is not false, hence is true, because it is not an empty string due to the space'''

# Write your code here:
print(bool(t))
print(bool(u))

# ============================================================
# EXERCISE 10 - TRICKY STRING VALUES
# ============================================================

"""Predict and print the Boolean value of each variable.

Remember that the values below are strings."""

v = "False"
z = "0"
x = "None"

# Write your predictions as comments:
# v: True
# z: True
# x: True

# Write your code here:
print(bool(v))
print(bool(z))
print(bool(x))



# ============================================================
# EXERCISE 11 - CHECK DATA TYPES
# ============================================================

"""Use isinstance() to check whether:

- value_1 is an integer
- value_1 is a string
- value_2 is a string
- value_3 is a float

Print all four results."""

value_1 = 200
value_2 = "200"
value_3 = 2.5

# Write your code here:
print(isinstance(value_1, int))
print(isinstance(value_1, str))
print(isinstance(value_2, str))
print(isinstance(value_3, float))


# ============================================================
# EXERCISE 12 - SAVE BOOLEAN RESULTS
# ============================================================

"""Create and save Boolean results for these questions:

- Is temperature greater than 20?
- Is city equal to "Lausanne"?
- Is "Python" present in skills?
- Is username non-empty when evaluated with bool()?

Print each result with a descriptive f-string."""

temperature = 22
city = "Lausanne"
skills = "Python, SQL and Excel"
username = "Nicola"

# Write your code here:
print(f"Is temperature greater than 20? {temperature > 20} \n"
      f"Is city equal to Lausanne? {city == "Lausanne"} \n"
      f"Is Python present in skills? {"Python" in skills} \n"
      f"Is username non-empty when evaluated with bool()? {bool(username)}")



# ============================================================
# EXERCISE 13 - FINAL DAY 5 CHALLENGE
# ============================================================

"""Create a small eligibility checker using only Day 1-5 ideas.

Requirements:

1. Create variables for your name, age, city, preferred language
   and whether you are currently studying.
2. Check whether the name has content using bool().
3. Check whether the age is at least 18.
4. Check whether the city equals "Lausanne".
5. Check whether the preferred language equals "Python".
6. Check whether the name contains only letters after removing
   its spaces with replace().
7. Use isinstance() to check whether age is an integer.
8. Save every result in a clearly named variable.
9. Print every result using descriptive f-strings.

Do not use an if statement. That topic will be covered later."""

# Write your code here:
name_1 = "Nicola"
age_1 = 32
city_1 = "Lausanne"
preferred_language = "English"
currently_studying = True

print(f"The variable name_1 has content? {bool(name_1)}")
print(f"Is my age greater than 18? {age_1 >= 18}")
print(f"Is the city_1 equal to Lausanne? {city_1 == "Lausanne"}")
print(f"Does your preferred language equal to Python? {preferred_language == "Python"}")
print(f"Does name_1 contains only letter? {name_1.replace(" ", "").isalpha()}")
print(f"Is age an integer? {isinstance(age_1, int)}")

name_has_content = bool(name_1)
age_is_at_least_18 = age_1 >= 18
city_is_lausanne = city_1 == "Lausanne"
language_is_python = preferred_language == "Python"
name_contains_only_letters = name_1.replace(" ", "").isalpha()
age_is_integer = isinstance(age_1, int)

print(f"Does the name have content? {name_has_content}")
print(f"Is the age at least 18? {age_is_at_least_18}")
print(f"Is the city Lausanne? {city_is_lausanne}")
print(f"Is the preferred language Python? {language_is_python}")
print(f"Does the name contain only letters? {name_contains_only_letters}")
print(f"Is the age an integer? {age_is_integer}")