# Exercise 1
unit = input("Enter the unit to convert (C for Celsius, F for Fahrenheit): ")
temperature = float(input("Enter the temperature: "))

if unit.lower() == 'c':
  fahrenheit = (temperature * 9/5) + 32
  print("Temperature in Fahrenheit:", fahrenheit)
elif unit.lower() == 'f':
  celsius = (temperature - 32) * 5/9
  print("Temperature in Celsius:", celsius)
else:
  print("Invalid unit input")
