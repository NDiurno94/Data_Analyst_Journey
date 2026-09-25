# ============================================================
# ARITHMETIC OPERATORS
# ============================================================

"""
+   addition          
-   subtraction
*   multiplication    
/   division
//  floor division    
%   remainder (modulo)
**  exponentiation (power)

For integer operands, / still returns a float.
Do not divide by zero: /, // and % raise ZeroDivisionError
when their right operand is zero."""

a = 17
b = 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(a ** 2)  # 289
print(20 / 5)  # 4.0


# ============================================================
# FLOOR DIVISION AND REMAINDERS
# ============================================================

"""Imagine packing 23 items into boxes that each hold 6 items.
// gives the number of full boxes; 
% gives the leftover items.

Floor division rounds DOWN, towards negative infinity.
It does not simply remove the decimal part.
With a positive divisor, the remainder is non-negative."""

items = 23
box_size = 6
print(items // box_size)  # 3
print(items % box_size)   # 5
print(-17 // 5)           # -4
print(-17 % 5)            # 3: (-4 * 5) + 3 equals -17

"""A number is EVEN when division by 2 leaves no remainder."""

print(14 % 2 == 0)  # True
print(15 % 2 == 0)  # False


# ============================================================
# THE SAME SYMBOL CAN WORK WITH DIFFERENT TYPES
# ============================================================

"""With strings, + joins text and * repeats it.
Convert a number before joining it to text, or use an f-string."""

print(12 + 4)              # 16
print("12" + "4")          # 124
print("Python " * 3)       # Python Python Python (trailing space)
print("Day " + str(6))     # Day 6
print(f"Day {6}")          # Day 6
# print("Day " + 6)        # TypeError; kept as a comment


