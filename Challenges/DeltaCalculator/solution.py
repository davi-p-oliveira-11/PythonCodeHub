def calculate_area():
    value_a = int(input('Enter the value of A '))
    value_b = int(input('Enter the value of B '))
    value_c = int(input('Enter the value of C '))

    # bhaskara:  delta = b² - 4ac
    value_delta = (value_b ** 2) - 4 * (value_a * value_c)
    print(f'The value of delta is equal to {value_delta}')


calculate_area()
input("Press Enter to Exit ... ")
