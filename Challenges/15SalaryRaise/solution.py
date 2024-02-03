def rent_calc():
    distance_traveled = int(input("How many kilometers were traveled with the rented car ? "))
    days_rented = int(input("For how many days was the car rented ? "))

    cost_for_days = days_rented * 90
    cost_for_distance = distance_traveled * 0.2
    total_cost = cost_for_days + cost_for_distance

    print(f'''
     The client traveled {distance_traveled} km with the car, 
rented the car for {days_rented} days, which cost {cost_for_days} 
USD for the rented days, and {cost_for_distance:.2f} USD for the kilometers traveled. 
The total cost that the client must pay is: {total_cost:.2f} USD.
''')


rent_calc()
input("Press Enter to Exit ... ")
