# ============================================================
# OPTIONAL EXTENSION - BITWISE OPERATORS
# ============================================================

"""Integers can be written in binary using 0 and 1 digits.
The rightmost places represent 1, 2, 4, 8, and so on.
6 is 0110 (4 + 2); 3 is 0011 (2 + 1).

&  keeps a bit when both input bits are 1
|  keeps a bit when at least one input bit is 1
^  keeps a bit when the input bits differ
~  inverts bits; for Python integers, ~n equals -(n + 1)
<< shifts bits left; shifting by 1 multiplies by 2
>> shifts bits right; shifting by 1 floor-divides by 2

Do not substitute & and | for and and or in today's Boolean
checks. ^ means bitwise XOR, not exponentiation.
Bitwise operations are an introduction only today."""

print(6 & 3)   # 2  (0010)
print(6 | 3)   # 7  (0111)
print(6 ^ 3)   # 5  (0101)
print(~6)      # -7
print(6 << 1)  # 12
print(6 >> 1)  # 3

"""Bitwise operators also have assignment forms:
&=, |=, ^=, <<= and >>=. For example:"""

flags = 6
flags &= 3
print(flags)  # 2


