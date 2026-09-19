# Day 4 - Python Strings

## What Is a String?

A string is a sequence of characters used to store text. In Python, strings use the `str` data type and are written inside single or double quotation marks.

```python
name = "Nicola"
city = 'Lausanne'
```

Day 4 builds on variables, data types and casting from the earlier lessons. It focuses on creating, accessing, extracting, modifying and formatting text.

## What Is Covered in Day 4?

- Creating strings with single and double quotes.
- Using quotation marks inside strings.
- Creating multiline strings with triple quotes.
- Accessing individual characters with indexes.
- Understanding that indexing begins at `0`.
- Using negative indexes to count from the end.
- Finding the length of a string with `len()`.
- Checking for text with `in` and `not in`.
- Extracting part of a string with slicing.
- Using omitted and negative slice indexes.
- Changing case with `upper()`, `lower()`, `capitalize()` and `title()`.
- Removing outer whitespace with `strip()`, `lstrip()` and `rstrip()`.
- Replacing text with `replace()`.
- Splitting text with `split()`.
- Finding and counting text with `find()` and `count()`.
- Checking content with methods such as `startswith()`, `endswith()`, `isalpha()`, `isdigit()` and `isalnum()`.
- Joining strings with the `+` operator.
- Combining text and variables with f-strings.
- Formatting decimal values inside f-strings.
- Adding quotes, new lines, tabs and backslashes with escape characters.
- Understanding that strings are immutable.

## Objectives

By the end of Day 4, I should be able to:

- Create and print single-line and multiline strings.
- Access characters safely using positive and negative indexes.
- Extract the required part of a string with slicing.
- Check a string's length and whether it contains particular text.
- Clean and standardise text with common string methods.
- Understand that a method returns a new string rather than changing the original.
- Join strings and deliberately add spaces between words.
- Insert strings and numbers into readable sentences with f-strings.
- Display decimal numbers to a chosen precision.
- Use common escape characters correctly.
- Combine several string operations in a small program.

## Files

- `strings.py` - Introduces strings, quotation marks, multiline strings, indexing, `len()`, membership checks and immutability.
- `string_slicing.py` - Covers start and end indexes, omitted indexes and negative slicing.
- `string_methods.py` - Covers the most useful beginner methods for cleaning, changing, splitting, finding and checking text.
- `string_formatting.py` - Covers concatenation, f-strings, placeholders, decimal formatting and escape characters.
- `exercises.py` - Contains progressive practice exercises and a final Day 4 challenge.

## Important Rules to Remember

### Indexes begin at zero

```python
word = "Python"
print(word[0])  # P
```

### A slice excludes its end index

```python
word = "Python"
print(word[0:3])  # Pyt
```

### Strings cannot be changed in place

```python
word = "python"
new_word = word.upper()

print(word)      # python
print(new_word)  # PYTHON
```

### Concatenation does not add spaces automatically

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

### F-strings can include different data types

```python
name = "Nicola"
age = 32

print(f"My name is {name} and I am {age} years old.")
```

## Suggested Study Order

1. Run `strings.py` and change some of the values.
2. Practise predicting indexes before running `string_slicing.py`.
3. Run `string_methods.py` and compare each original string with its returned value.
4. Run `string_formatting.py` and practise building your own sentences.
5. Complete `exercises.py` without looking at the theory files whenever possible.

## Practice Advice

Run the program after every small change. Before running it, predict the output. If an index or slice gives an unexpected result, write the indexes above the word on paper and remember that the first character is index `0`.

The exercises deliberately reuse personal and data-analysis examples so that the syntax is easier to remember. Avoid copying the examples directly: type each answer yourself and test it.

## Day 4 Outcome

At the end of Day 4, I should be comfortable working with text in Python. I should be able to select characters, extract sections, clean inconsistent text and create readable output containing both words and numbers.

These skills are essential for later work with user input, files and real datasets, where text often needs to be checked, cleaned and reformatted before analysis.

