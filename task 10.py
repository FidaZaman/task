temp = input("Enter the unit to convert [C for Celsius, F for Fahrenheit]: ")
temperature = float(input("Enter the temperature: "))

if temp.lower()=='c':
    far = (temperature*9/5)+32
    print("Temperature in Fahrenheit:", far)
elif temp.lower()=='f':
    cel = (temperature-32)*5/9
    print("Temperature in Celsius:", cel)
else:
    print("Invalid unit input")
