def ink_needed():
    height = float(input('Enter the height of the wall in meters: '))
    width = float(input('Enter the width of the wall in meters: '))

    area = width * height
    amountNeeded = area * 0.5

    print(f'The area of the wall to be painted is {area} square meters.')
    print(f'and the amount of paint needed to paint the wall is {amountNeeded} liters.')


ink_needed()
input("Press Enter to Exit ... ")
