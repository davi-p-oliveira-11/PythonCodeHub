def operations():
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter another number: "))

    sum = number_1 + number_2
    subtraction = number_1 - number_2
    multiplication = number_1 * number_2
    division = number_1 * number_2
    exponentiation = number_1 ** number_2
    modulo = number_1 % number_2

    print(f'''The sum of {number_1} and {number_2} is equal to {sum}
  The subtraction of {number_1} by {number_2} is equal to {subtraction}
  The multiplication of {number_1} by {number_2} is equal to {multiplication}
  The division of {number_1} by {number_2} is equal to {division}
  The exponentiation of {number_1} to the power of {number_2} is equal to ${exponentiation}
  The modulo of {number_1} divided by {number_2} is equal to {modulo}
  ''')


operations()
input("Press Enter to Exit ... ")
