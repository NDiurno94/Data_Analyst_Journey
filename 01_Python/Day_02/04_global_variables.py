'''A global variable is a variable that is created outside
of a function.

A global variable can be accessed both outside and inside
a function.

In the example below, "x" is created outside the function,
so it is a global variable.'''

x = "awesome"    # Global variable


def myfunc():
    print("Python is " + x)


myfunc()    # Output: Python is awesome


# ============================================================
# GLOBAL AND LOCAL VARIABLES
# ============================================================

'''If you create a variable inside a function, that variable
is normally local to that function.

A local variable can only be used inside the function where
it was created.

If a local variable has the same name as a global variable,
Python treats them as two separate variables.'''

y = "awesome"    # Global variable


def myfunc():
    y = "fantastic"    # Local variable
    print("Python is " + y)


myfunc()                   # Output: Python is fantastic
print("Python is " + y)    # Output: Python is awesome


# ============================================================
# THE GLOBAL KEYWORD
# ============================================================

'''The global keyword can be used to create a global variable
from inside a function.

Normally, a variable created inside a function is local.
Using the global keyword makes it belong to the global scope.'''


def myfunc():
    global z
    z = "fantastic"


myfunc()

print("Python is " + z)    # Output: Python is fantastic


# ============================================================
# CHANGING A GLOBAL VARIABLE INSIDE A FUNCTION
# ============================================================

'''The global keyword can also be used when you want to change
the value of an existing global variable from inside a function.

Without the global keyword, assigning a value inside the function
would create a separate local variable instead.'''

a = "awesome"


def myfunc():
    global a
    a = "fantastic"


myfunc()

print("Python is " + a)    # Output: Python is fantastic