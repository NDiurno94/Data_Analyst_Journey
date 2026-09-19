# Day 5 - Python Booleans

## What Is a Boolean?

A Boolean represents one of two possible values: `True` or `False`. Its Python data type is `bool`.

```python
learning_python = True
finished_course = False

print(type(learning_python))  # <class 'bool'>
```

Booleans are useful whenever a program needs the answer to a yes-or-no question. For example: Is one number larger than another? Are two values equal? Does a string contain a particular word?

## Important Syntax

`True` and `False` must begin with capital letters and must not use quotation marks.

```python
correct = True       # Boolean
text = "True"        # String
```

Although these values look similar when printed, they have different data types.

## What Is Covered in Day 5?

- Understanding the `bool` data type.
- Creating variables containing `True` and `False`.
- Distinguishing Booleans from strings.
- Producing Boolean results by comparing values.
- Understanding `=`, `==` and `!=`.
- Comparing numeric and string values.
- Recognising that string comparisons are case-sensitive.
- Reviewing string operations that return Booleans.
- Evaluating values with `bool()`.
- Recognising truthy and falsy values.
- Understanding the difference between an empty string and a space.
- Checking a value's data type with `isinstance()`.
- Saving Boolean results in clearly named variables.
- Displaying Boolean results with f-strings.

## Comparison Symbols Introduced

| Symbol | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `5 <= 10` | `True` |

These comparisons are introduced only to demonstrate how Boolean results are created. Operators will be studied in greater detail in the next lesson.

## Truthy and Falsy Values

The `bool()` function evaluates a value and returns either `True` or `False`.

Most values are truthy. Examples include:

- Non-empty strings.
- Non-zero numbers, including negative numbers.
- Non-empty lists, tuples, sets and dictionaries.

```python
print(bool("Python"))  # True
print(bool(32))        # True
print(bool(-1))        # True
```

The main falsy values are:

- `False`
- `None`
- Numeric zero, including `0` and `0.0`
- An empty string: `""`
- Empty collections such as `[]`, `()`, `{}` and `set()`

```python
print(bool(""))    # False
print(bool(0))     # False
print(bool([]))    # False
```

Be careful: a string containing a space is not empty.

```python
print(bool(""))   # False
print(bool(" "))  # True
```

Similarly, `"False"` and `"0"` are both truthy because they are non-empty strings.

## Objectives

By the end of Day 5, I should be able to:

- Explain what a Boolean value represents.
- Create and recognise Boolean variables.
- Predict the result of simple comparisons.
- Distinguish assignment with `=` from comparison with `==`.
- Use `bool()` to evaluate values and variables.
- Recognise common truthy and falsy values.
- Understand that strings containing text are truthy, even when that text says `False`.
- Recognise Boolean results returned by string checks.
- Use `isinstance()` to check a value's type.
- Store Boolean results in descriptive variables.

## Files

- `booleans.py` - Complete theory with examples of Boolean values, comparisons, `bool()`, truthy and falsy values, string checks and `isinstance()`.
- `exercises.py` - Thirteen progressive exercises, finishing with a Boolean eligibility challenge.

## Suggested Study Order

1. Run `booleans.py` one section at a time.
2. Before running each section, predict every `True` or `False` result.
3. Change the values and observe which results change.
4. Complete `exercises.py` without looking at the theory whenever possible.
5. Explain each answer aloud: do not only state the result—explain why Python returns it.

## Common Mistakes

### Using lowercase Boolean names

```python
learning = true  # Incorrect
learning = True  # Correct
```

### Putting quotation marks around a Boolean

```python
answer = "False"  # This is a non-empty string
print(bool(answer)) # True
```

### Confusing assignment and comparison

```python
age = 32      # Assigns 32 to age
age == 32     # Checks whether age equals 32
```

### Assuming a space is an empty string

```python
print(bool(""))   # False
print(bool(" "))  # True
```

## Day 5 Outcome

At the end of Day 5, I should understand how Python represents yes-or-no information and how comparisons produce Boolean results. I should be able to evaluate common values, recognise important edge cases and store checks in clearly named variables.

These concepts prepare the foundation for operators and conditional statements, where Boolean results will control which parts of a program run.
