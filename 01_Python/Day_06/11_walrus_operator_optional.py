# ============================================================
# OPTIONAL PREVIEW - THE WALRUS OPERATOR
# ============================================================

""":= assigns a value while also producing that value inside
an expression. It requires Python 3.8 or later.
Ordinary = assignment is clearer for today's exercises."""

print(current_total := 12 + 8)  # 20
print(current_total)           # 20
