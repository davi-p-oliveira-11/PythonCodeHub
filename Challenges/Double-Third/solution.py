def double_third():
    number = float(input('Enter a number'))

    double = number * 2
    one_third = number / 3

    print(f'The double of {number} is {double}')

    # Format the string to display with 2 decimal places
    print(f'The third part of {number} is {one_third:.2f}')


double_third()
input("Press Enter to Exit ... ")
