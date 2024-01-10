input_str = input("Enter a string: ")
print(input_str[::-1])

# no. 12
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
