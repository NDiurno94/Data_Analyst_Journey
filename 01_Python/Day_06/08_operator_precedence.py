# ============================================================
# OPERATOR PRECEDENCE
# ============================================================

"""Precedence decides how an expression is grouped.
For the everyday operators used here, higher priority comes first:

1. Parenthesised expressions
2. **
3. *, /, //, %
4. +, -
5. Comparisons, membership and identity checks
6. not
7. and
8. or

Operators on the same arithmetic level usually group left to
right. Powers group right to left. Use parentheses for clarity.
This is a practical guide, not Python's full precedence table."""

print(4 + 3 * 2)          # 10
print((4 + 3) * 2)        # 14
print(24 / 4 * 2)         # 12.0
print(2 ** 3 ** 2)        # 512: 2 ** (3 ** 2)
print((2 ** 3) ** 2)      # 64
print(-3 ** 2)            # -9: -(3 ** 2)
print((-3) ** 2)          # 9
print(True or False and False)    # True
print((True or False) and False)  # False


