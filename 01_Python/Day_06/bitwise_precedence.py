"""DAY 5 - BITWISE OPERATORS AND OPERATOR PRECEDENCE

Bitwise operators are included because they are part of Python operators,
but they are not a priority for a beginner data-analysis path.
"""


# ============================================================
# 1. BITWISE OPERATORS
# ============================================================

# Bitwise operators work with the binary representation of integers.

x = 6   # binary: 110
y = 3   # binary: 011

print(x & y)   # AND:  010 -> 2
print(x | y)   # OR:   111 -> 7
print(x ^ y)   # XOR:  101 -> 5
print(~x)      # NOT: -7
print(x << 1)  # Left shift:  1100 -> 12
print(x >> 1)  # Right shift: 0011 -> 3


# For now, recognise these operators. You do not need to memorise
# their binary behaviour before moving to the next Python topic.


# ============================================================
# 2. OPERATOR PRECEDENCE
# ============================================================

# Python follows an order of operations.
# Multiplication is evaluated before addition.

result = 2 + 3 * 4
print(result)  # 14


# Parentheses are evaluated first and make the intention clear.

result = (2 + 3) * 4
print(result)  # 20


# Exponentiation is evaluated before multiplication.

result = 2 * 3 ** 2
print(result)  # 18


# Comparisons happen after arithmetic operations.

result = 5 + 5 > 8
print(result)  # True


# not is evaluated before and; and is evaluated before or.

result = True or False and False
print(result)  # True


# Prefer parentheses when combining different kinds of operators.

result = True or (False and False)
print(result)  # True


# ============================================================
# SUMMARY
# ============================================================

# &   bitwise AND
# |   bitwise OR
# ^   bitwise XOR
# ~   bitwise NOT
# <<  left shift
# >>  right shift
# Use parentheses to control or clarify evaluation order.

