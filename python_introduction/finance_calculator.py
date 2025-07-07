# calculating monthly savings based on inputted monthly income and expenses at a fixed rate of 5%.
month_income = float(input("Enter your monthly income: "))
total_month_expenses = float(input("Enter your total monthly expenses: "))
month_savings = month_income - total_month_expenses
projected_savings = month_savings * 12 + (month_savings * 12 * 0.05)

print(f"Your monthly savings are {month_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")