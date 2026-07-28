# ============================================================
# PYTHON INDENTATION
# ============================================================

'''Indentation refers to the spaces at the beginning of a line
of code.

Indentation is very important in Python because it is used to
define blocks of code.

In the example below, the indented print() statement belongs
to the if statement above it.'''

if 5 > 2:
    print("Five is greater than two!")

'''If the print() statement was not indented, Python would
raise an IndentationError.

For example, the following code would be incorrect:

if 5 > 2:
print("Five is greater than two!")

Python also requires indentation to be consistent within the
same block of code.

The standard convention in Python is to use 4 spaces for each
level of indentation.'''


# ============================================================
# INTRODUCTION TO PYTHON VARIABLES
# ============================================================

'''A variable is a name used to store a value.

A value is assigned to a variable using the equals sign (=).

In this example, "age" stores a number and "message" stores
a piece of text.'''

age = 30
message = "Hello, World!"

print(age)
print(message)

'''Variables can also be used inside other statements and
mathematical operations.'''

print("The value of age is:", age)
print("The message is:", message)
print("The sum of age and 10 is:", age + 10)

'''Variables will be covered in much more detail during Day 2.'''


# ============================================================
# PYTHON STATEMENTS
# ============================================================

'''A statement is an instruction that Python can execute.

A Python program normally contains multiple statements, which
are executed in order from top to bottom.'''

print("This is the first statement.")
print("This is the second statement.")
print("This is the third statement.")

'''Python also allows multiple statements to be written on the
same line by separating them with a semicolon (;).'''

print("First statement"); print("Second statement")

'''Although this is valid Python, writing separate statements
on separate lines is usually easier to read and is preferred.'''


# ============================================================
# THE PRINT() FUNCTION
# ============================================================

'''The print() function is used to display information in the
terminal.

It can display text, numbers and multiple values.'''

print("Hello, World!")
print(25)
print("I am", 30, "years old.")

'''By default, every print() starts its output on a new line.

The end parameter can be used to change what Python prints at
the end of the statement.'''

print("Hello", end=" ")
print("World!")

# Output: Hello World!


# ============================================================
# PYTHON NUMBERS
# ============================================================

'''Python can work with different types of numbers.

Whole numbers are called integers, while numbers containing
a decimal point are called floating-point numbers (floats).'''

print(3)       # Integer
print(-5)      # Negative integer
print(3.14)    # Float


# ============================================================
# BASIC MATHEMATICAL OPERATIONS
# ============================================================

'''Python can perform mathematical operations directly.

For example, the + operator performs addition and the *
operator performs multiplication.'''

print(3 + 5)    # Output: 8
print(3 * 4)    # Output: 12

'''Mathematical operations can also be performed inside a
print() function together with text.'''

print("The sum of 3 and 5 is:", 3 + 5)
print("The product of 3 and 4 is:", 3 * 4)
print("I am", 25 + 5, "years old.")