# ============================================================
# PYTHON VARIABLES - EXERCISES
# ============================================================

'''Complete each exercise using what you have learned about
Python variables.

Try to complete the exercises without looking at the theory files.
Run the file after each exercise to check your code.'''


# ============================================================
# EXERCISE 1 - CREATING VARIABLES
# ============================================================

'''Create four variables:

- name containing your name
- age containing your age
- height containing your height in metres
- learning_python containing True

Print all four variables separately below.'''

# Write your code here:



# ============================================================
# EXERCISE 2 - CHECKING DATA TYPES
# ============================================================

'''Using the four variables from Exercise 1, print the data type
of each variable using type().

Before running the program, try to predict what each type will be.'''

# Write your code here:



# ============================================================
# EXERCISE 3 - CHANGING A VARIABLE
# ============================================================

'''Create a variable called score and give it the value 10.

Print score.

Then change the value of score to 25 and print it again.

Finally, change score to the string "Excellent" and print it again.'''

# Write your code here:



# ============================================================
# EXERCISE 4 - CASTING
# ============================================================

'''Create a variable called number containing the string "50".

1. Print its data type.
2. Convert number into an integer.
3. Print its data type again.
4. Convert number into a float.
5. Print both its value and data type.'''

# Write your code here:



# ============================================================
# EXERCISE 5 - VARIABLE NAMES
# ============================================================

'''Which of the following are valid Python variable names?

Do NOT uncomment the invalid ones.

Create the valid variables and assign any value to them.

first_name
2nd_name
my-age
country2
_my_variable
my variable
MY_SCORE'''

# Write your code here:



# ============================================================
# EXERCISE 6 - MULTIPLE ASSIGNMENT
# ============================================================

'''In ONE line of code, create three variables:

fruit = "Apple"
vegetable = "Carrot"
drink = "Water"

Then print all three variables using ONE print() function.'''

# Write your code here:



# ============================================================
# EXERCISE 7 - UNPACKING
# ============================================================

'''The following list has already been created for you.

Unpack the three values into three variables called
country, city and language.

Then print each variable separately.'''

information = ["Italy", "Rome", "Italian"]

# Write your code here:



# ============================================================
# EXERCISE 8 - STRING CONCATENATION
# ============================================================

'''Create two variables:

first_name = "Nicola"
last_name = "Diurno"

Using the + operator, print:

Nicola Diurno

Remember that you need a space between the two names.'''

# Write your code here:



# ============================================================
# EXERCISE 9 - DIFFERENT DATA TYPES
# ============================================================

'''The variables below have already been created.

Make Python print:

Nicola is 32 years old

You MUST use the + operator.

Think about what needs to happen to the age variable before
it can be concatenated with strings.'''

name = "Nicola"
age = 32

# Write your code here:



# ============================================================
# EXERCISE 10 - GLOBAL AND LOCAL VARIABLES
# ============================================================

'''Study the code below BEFORE running it.

Try to predict the two outputs.

Then run the program and check whether your prediction was correct.'''

word = "Python"


def show_word():
    word = "Variables"
    print(word)


show_word()
print(word)

# Write your predicted outputs here as comments:
# Output 1:
# Output 2:


# ============================================================
# EXERCISE 11 - GLOBAL KEYWORD
# ============================================================

'''Complete the function below so that it changes the global
variable status from "Learning" to "Completed".

You should use the global keyword.

The final print() should output:

Completed
'''

status = "Learning"


def change_status():
    # Write your code inside the function:
    pass


change_status()

print(status)


# ============================================================
# EXERCISE 12 - FINAL CHALLENGE
# ============================================================

'''Create a small personal profile using variables.

Create variables containing:

- your first name
- your last name
- your age
- your height
- whether you are learning Python (True/False)

Then print ONE line that looks like:

My name is Nicola Diurno, I am 32 years old and my height is 1.70 metres.

Requirements:

1. Use separate variables for the information.
2. Use the + operator to build the sentence.
3. Convert any variables when necessary using str().
4. Print the type of every variable after printing the sentence.

Try to complete this without looking at your previous files.'''

# Write your code here: