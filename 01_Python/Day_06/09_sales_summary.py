# ============================================================
# PRACTICAL EXAMPLE - A SMALL SALES SUMMARY
# ============================================================

"""Combine arithmetic and Boolean checks in a readable report.
Use descriptive variables so each calculation is easy to follow.
In an f-string, :.2f displays two decimal places."""

units_sold = 24
unit_price = 15
cost_per_unit = 9
sales_target = 300
region = "Lausanne"

revenue = units_sold * unit_price
total_cost = units_sold * cost_per_unit
profit = revenue - total_cost
target_reached = revenue >= sales_target
successful_local_day = target_reached and region == "Lausanne"

print(f"Revenue: {revenue:.2f}")                  # Revenue: 360.00
print(f"Profit: {profit:.2f}")                    # Profit: 144.00
print(f"Target reached: {target_reached}")        # Target reached: True
print(f"Successful local day: {successful_local_day}")  # True


