# ============================================================
# DAY 4 - PYTHON STRINGS EXERCISES
# ============================================================

"""Complete each exercise using what you learned during Day 4.

Try not to look at the theory files. Run the file after every
exercise and read each expected result carefully.
"""


# ============================================================
# EXERCISE 1 - CREATE STRINGS
# ============================================================

"""Create three variables containing:

- your first name
- your surname
- the city where you currently live

Print each variable and its data type."""

# Write your code here:

name = "Nicola"
surname = "Diurno"
city = "Lausanne"

print(name, type(name))

print(surname, type(surname))

print(city, type(city))


# ============================================================
# EXERCISE 2 - QUOTES AND MULTILINE STRINGS
# ============================================================

"""Print these two sentences using suitable quotation marks:

It's a great day to learn Python.
Nicola said, "I am learning strings."

Then create and print a multiline string containing three lines."""

# Write your code here:

first = "It's a great day to learn Python"
second = 'Nicola said, "I am learning strings'

print(first)

print(second)

third = """I moved to Lausanne on the 17th.
I am looking for a job.
Unfortunately, I am not able to find one."""

print(third)


# ============================================================
# EXERCISE 3 - ACCESS CHARACTERS
# ============================================================

"""Use the variable below.

Print the first, third and final characters using indexes.
Do not type the characters directly in print()."""

a = "Python"

# Write your code here:

print(a[0])

print(a[2])

print(a[5])

# ============================================================
# EXERCISE 4 - STRING LENGTH
# ============================================================

"""Print the number of characters in each string using len().
Predict both results before running the code."""

b = "Data"
c = "Data Analysis"

# Write your predictions as comments:

# b: 4
# c: 13

# Write your code here:

print(len(b))

print(len(c))

# ============================================================
# EXERCISE 5 - CHECK TEXT
# ============================================================

"""Use in and not in to check whether:

- "Python" is present
- "SQL" is present
- "Java" is absent

Print all three Boolean results."""

d = "I am learning Python and SQL"

# Write your code here:

print("Python" in d)

print("SQL" in d)

print("Java" in d)

# ============================================================
# EXERCISE 6 - BASIC SLICING
# ============================================================

"""Use slicing on the string below to print:

- "Data"
- "Analysis"
- the whole string

Do not type those words directly in print()."""

e = "Data Analysis"

# Write your code here:

print(e[:4])

print(e[5:])

print(e[:])

# ============================================================
# EXERCISE 7 - NEGATIVE INDEXING AND SLICING
# ============================================================

"""Use negative indexes to print:

- the final character
- the word "World"
- the final six characters, including the exclamation mark"""

f = "Hello, World!"

# Write your code here:

print(f[-1])

print(f[-6:-1])

print(f[-6:])

# ============================================================
# EXERCISE 8 - CHANGE LETTER CASE
# ============================================================

"""Print the string below in:

- upper case
- lower case
- title case
- sentence case using capitalize()"""

g = "pYTHON for DATA analysis"

# Write your code here:

print(g.upper())

print(g.lower())

print(g.title())

print(g.capitalize())


# ============================================================
# EXERCISE 9 - REMOVE WHITESPACE
# ============================================================

"""Use strip(), lstrip() and rstrip() on the variable below.
Print each result."""

h = "   Lausanne   "

# Write your code here:

print(h.strip())

print(h.lstrip())

print(h.rstrip())

# ============================================================
# EXERCISE 10 - REPLACE AND SPLIT
# ============================================================

"""Use replace() to change "Excel" to "Python".
Then split the second string at every comma and print the list."""

i = "I am learning Excel"
j = "Python,SQL,Excel"

# Write your code here:

print(i.replace("Excel", "Python"), type(i))

print(j.split(","), type(j))


# ============================================================
# EXERCISE 11 - FIND AND COUNT
# ============================================================

"""Using the word below:

- find the index of the first "n"
- find the index of "z"
- count how many times "a" appears

Print all three results."""

k = "ananas"

# Write your code here:

print(k.find("n"))

print(k.find("z"))

print(k.count("a"))


# ============================================================
# EXERCISE 12 - CHECK STRING CONTENT
# ============================================================

"""Use suitable methods to check whether:

- l starts with "Py"
- l ends with "on"
- l contains only letters
- m contains only digits
- n contains only letters and numbers

Print each result."""

l = "Python"
m = "2026"
n = "Python3"

# Write your code here:

print(l.startswith("Py"))

print(l.endswith("on"))

print(l.isalpha())

print(l.isdigit())

print(l.isalnum())

# ============================================================
# EXERCISE 13 - CONCATENATION
# ============================================================

"""Join the variables with + and print exactly:

Nicola Diurno lives near Lausanne

Remember to add the necessary spaces."""

first_name = "Nicola"
surname_1 = "Diurno"
city_1 = "Lausanne"

# Write your code here:

print(first_name + " " + surname_1 + " lives near " + city_1)


# ============================================================
# EXERCISE 14 - F-STRINGS
# ============================================================

"""Use one f-string and the variables below to print:

My name is Nicola, I am 32 years old and I am 1.7 metres tall.

Do not convert the numbers with str()."""

name_1 = "Nicola"
age = 32
height = 1.7

# Write your code here:

print(f"My name is, {name_1} I am {age} years old and I am {height} metres tall")

# ============================================================
# EXERCISE 15 - FORMAT A NUMBER
# ============================================================

"""Use an f-string and a format modifier to print exactly:

The total price is 19.50 CHF."""

price = 19.5

# Write your code here:

print(f"The total price is {price:.2f} CHF")

# ============================================================
# EXERCISE 16 - ESCAPE CHARACTERS
# ============================================================

"""Use escape characters to:

1. Print: Nicola said, "I am learning Python."
2. Print "Python" and "SQL" and "Pandas" on separate lines with one print().
3. Print "Name:" and "Nicola" separated by a tab."""

# Write your code here:

print("Nicola said, \"I am learning Python.\"")

print("Python\n" \
      
"SQL\n" \
"Pandas")
print("Name:\tNicola")



# ============================================================
# EXERCISE 17 - FINAL DAY 4 CHALLENGE
# ============================================================

"""Create a small personal profile using only Day 1-4 concepts.

Requirements:

1. Create variables for your full name, city, profession, age and
   favourite programming language.
2. Remove unwanted outer spaces from the name and city.
3. Correct their capitalisation with title().
4. Print the cleaned name and city.
5. Print the length of the cleaned full name.
6. Print the first and final characters of the cleaned name.
7. Print the first name using slicing.
8. Check whether "Python" is your favourite language.
9. Use replace() to change one word in the profession.
10. Use one f-string to print a complete profile sentence.

Choose your own values, but do not type them directly inside the
final profile sentence."""

# Write your code here:

full_name = "   nicola diurno   "
place = "   lausanne  "
profession = "bartender"
old = "32"
programming_language = ["Python", "Java", "SQL"]



print(f"My full name is {full_name.strip().title()}, and the city where I live at the moment is {place.strip().title()}.")

print(len(full_name.strip()))

print(f"The first character is <{full_name.strip().title()[0]}>, and the last character is <{full_name.strip().title()[12]}>.")

print(f"My name is: {full_name.strip().title()[0:6]}.")

print(f"Is Python my favourite programming language? {"Python" in programming_language}")

print(f"I am a {profession.title()}, but I am studying to became a {profession.replace("bartender", "Data Analyst")} in future.")

print(f"Hello everyone, my name is {full_name.strip().title()}, I am {old} years old, and I recently moved to {place.strip().title()},\n" \
f"where I am looking for a job as {profession.title()}, while studying to became {profession.replace("bartender", "Data Analyst")}.")