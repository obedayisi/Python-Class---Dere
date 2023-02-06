# Write a program that converts Celsius to Fahrenheit

# Take user input in Celsius and 
print("\nThis program converts temperature from Celsius to Fahrenheit")
celsius = input("\nPlease enter a temperature in Celsius: ")
celsius = int(celsius)

# Convert Celsius to Fahrenheit
fahrenheit = celsius*(9/5) + 32

# Display Results
print(f"\nTemperature in Celsius is: {celsius}C")
print(f"\nTemperature in Fahrenheit is: {fahrenheit}F")

