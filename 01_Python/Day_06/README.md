# Day 6 - Python Operators

## What Is an Operator?

An operator performs an operation on a value or on values. In `18 * 3`, the `*` operator multiplies two numbers. Operators let me calculate results, update variables and combine the Boolean checks introduced on Day 5.

```python
units_sold = 35
unit_price = 18
revenue = units_sold * unit_price
target_reached = revenue >= 600
print(f"Revenue: {revenue}")                # Revenue: 630
print(f"Target reached: {target_reached}")  # Target reached: True
```

## What Is Covered in Day 6?

- Arithmetic and the differences between division, floor division and remainder.
- Updating numeric variables with assignment shortcuts.
- Reviewing all six comparison operators.
- Combining checks with `and`, `or` and `not`.
- Checking ranges and understanding short-circuit evaluation.
- Testing membership in strings and simple lists.
- Distinguishing equal values from identical objects.
- Using parentheses to make calculation order clear.
- Building a small sales report from named variables.
- Optional introductions to bitwise operators and `:=`.

No conditional statements, loops or function definitions are required. Lists appear only as small collections to demonstrate membership and identity.

## Arithmetic Reference

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `19 + 4` | `23` |
| `-` | Subtraction | `19 - 4` | `15` |
| `*` | Multiplication | `19 * 4` | `76` |
| `/` | Division | `19 / 4` | `4.75` |
| `//` | Floor division | `19 // 4` | `4` |
| `%` | Remainder | `19 % 4` | `3` |
| `**` | Power | `19 ** 2` | `361` |

`//` rounds down: `-19 // 4` is `-5`. Dividing by zero with `/`, `//` or `%` raises an error.

## Assignment and Comparison

For numbers, `total += 10` means `total = total + 10`. The same pattern applies to `-=`, `*=`, `/=`, `//=`, `%=` and `**=`.

| Purpose | Operators | Example |
|---|---|---|
| Assign a value | `=` | `score = 80` |
| Compare values | `==`, `!=`, `>`, `<`, `>=`, `<=` | `score >= 60` |
| Combine checks | `and`, `or`, `not` | `score >= 60 and score <= 100` |
| Check membership | `in`, `not in` | `"Python" in skills` |
| Check identity | `is`, `is not` | `result is None` |

## Logical Operators

For Boolean inputs, `and` requires both inputs to be true; `or` requires at least one; `not` reverses the truth value.

| First input | Second input | `and` | `or` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

With other types, `and` and `or` return an operand. For example, `"" or "Guest"` returns `"Guest"`. They evaluate the right side only when needed; the lecture demonstrates how this can guard a division.

## Common Mistakes

- **Confusing `=` and `==`:** `age = 32` stores a value; `age == 32` checks equality.
- **Confusing `^` and `**`:** `5 ** 2` is 25. `^` is bitwise XOR.
- **Treating `/` as integer division:** `20 / 5` is `4.0`.
- **Using `is` for value comparisons:** compare text and numbers with `==`. Use `is None` for a missing value.
- **Leaving out a comparison:** use `city == "Lausanne" or city == "Geneva"`. Writing `city == "Lausanne" or "Geneva"` leaves a truthy string on the right.
- **Ignoring precedence:** `6 + 4 * 3` is 18; `(6 + 4) * 3` is 30.
- **Assuming membership ignores case:** `"python" in "Python"` is `False`.

## Objectives

By the end of Day 6, I should be able to:

- Select the correct operator for a calculation.
- Explain the difference between `/`, `//` and `%`.
- Update a number using assignment shortcuts.
- Save and combine Boolean results in descriptive variables.
- Check membership and distinguish equality from identity.
- Predict common expressions and add parentheses for clarity.
- Calculate revenue, cost, profit and target checks in a small report.

Bitwise operators are optional awareness for today, not a prerequisite for moving on.

## Files and Study Order

Study the numbered topic files in order. Each file can run independently.

| File | Topic |
|---|---|
| `01_operators_intro.py` | What operators and expressions are |
| `02_arithmetic_operators.py` | Calculations, division, remainders and string operators |
| `03_assignment_operators.py` | Assigning and updating values |
| `04_comparison_operators.py` | Comparing values and checking ranges |
| `05_logical_operators.py` | Combining checks, truthy values and short-circuiting |
| `06_membership_operators.py` | Checking membership with `in` and `not in` |
| `07_identity_operators.py` | Equality versus identity and checking for `None` |
| `08_operator_precedence.py` | Calculation order and parentheses |
| `09_sales_summary.py` | A practical example combining operators |
| `10_bitwise_operators_optional.py` | Optional introduction to binary operations |
| `11_walrus_operator_optional.py` | Optional introduction to `:=` |
| `exercises.py` | All 16 exercise prompts with blank answer spaces |
| `exercises_completed.py` | An identical blank copy for your own completed work |

## Suggested Study Order

1. Read the numbered topic files from 01 to 09, running one section at a time.
2. Predict each output, then change a value and explain the new result.
3. Work through exercises 1-14 in `exercises_completed.py`, keeping `exercises.py` as your untouched reference.
4. Read optional topic files 10-11, then attempt optional exercises 15-16.

Both exercise files initially contain exactly the same prompts and starter variables. Neither contains solutions; the answer spaces are left for you to complete.

Use Python 3.8 or newer for the optional walrus example. No external packages are needed. Both exercise files run silently until you add answers.

## Day 6 Outcome

I should be able to turn raw values into useful calculations and clear Boolean checks. These skills prepare me to write conditions and, later, filter and analyse data.


