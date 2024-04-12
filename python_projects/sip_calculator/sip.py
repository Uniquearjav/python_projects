monthly_sip = int(input("Enter the monthly SIP amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_interest_rate = annual_interest_rate / 12 / 100
years = int(input("Enter the number of years: "))
total_amount = 0

for i in range(years * 12):
    total_amount = (total_amount + monthly_sip) * (1 + monthly_interest_rate)

print(f'Total amount after {years} years: {total_amount:.2f}')
