def brl_to_dollar():
    available_brl = float(input('Enter a value in BRL: '))
    today_usd = float(input("What is today's dollar exchange rate ? "))
    value_usd = available_brl / today_usd

    print(f'You can buy a total of {value_usd:.2f} USD')


brl_to_dollar()
input("Press Enter to Exit ... ")
