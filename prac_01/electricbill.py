TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

kWh_cents = str(input("Which TARIFF? 11 or 31: "))
daily_use = float(input("Enter daily use: "))
num_days = float(input("Enter number of billing days: "))

prompt = "Estimated Bill: $"

calc_11 = round(TARIFF_11 * daily_use * num_days, 2)
calc_31 = round(TARIFF_31 * daily_use * num_days, 2)

if kWh_cents == '11':
    print(prompt + str(calc_11))
else:
    print(prompt + str(calc_31))
