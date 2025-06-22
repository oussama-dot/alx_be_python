global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR
user = int(input("Enter the temperature to convert:"))
usertwo = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def  convert_to_celsius():
    FAHRENHEIT_TO_CELSIUS_FACTOR = (user-32) * 5/9 
    print(f"{user}°F is ",FAHRENHEIT_TO_CELSIUS_FACTOR,"°C")
    

def convert_to_fahrenheit():
    CELSIUS_TO_FAHRENHEIT_FACTOR = (user-32) * 9/5
    print(f"{user}°C is ",CELSIUS_TO_FAHRENHEIT_FACTOR,"°F")


if usertwo == "F":
   convert_to_fahrenheit()
else:
    convert_to_celsius()