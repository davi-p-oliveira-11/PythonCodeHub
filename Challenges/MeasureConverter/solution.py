def measure_converter():
    
  meters = float(input('Enter a distance in meters '))

  kilometers = meters / 1000
  hectometers = meters / 100
  decameters = meters / 10
  decimeters = meters * 10
  centimeters = meters * 100
  millimeters = meters * 1000


  print(f'''
   The distance of {meters:.2f}m ccorresponds to:
  {kilometers}Km
  {hectometers}Hm
  {decameters}Dam
  {decimeters}dm
  {centimeters}cm
  {millimeters}mm
  ''')


measure_converter()
input("Press Enter to Exit ... ")
