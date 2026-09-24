# ============================================================
# ASSIGNMENT AND UPDATING VARIABLES
# ============================================================

"""= stores a value. It does not ask whether values are equal.
For numbers, score += 5 is shorthand for score = score + 5.
The right side is calculated before the new value is stored.

Each update below uses the result of the previous line."""

score = 20
score += 5
print(score)  # 25
score -= 10
print(score)  # 15
score *= 2
print(score)  # 30
score /= 4
print(score)  # 7.5

number = 17
number //= 5
print(number)  # 3
number **= 3
print(number)  # 27
number %= 5
print(number)  # 2


