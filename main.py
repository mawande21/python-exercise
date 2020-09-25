#Salaries calculations
print("---Welcome to Employees Salary calculation--")

salary_amount = int(input("Please enter annual salary: "))
income_tax = float(input("Please enter income tax in decimal form: "))

gross_monthly_salary = salary_amount/12
monthly_tax_payable = (gross_monthly_salary * income_tax)/12
net_monthly_salary = gross_monthly_salary - monthly_tax_payable


if income_tax == 0.295 or income_tax == 0.25:
    print(gross_monthly_salary)
    print(monthly_tax_payable)
    print(net_monthly_salary)
else:
    print("Please restart and check the income tax")
