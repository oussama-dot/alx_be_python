global FAHRENHEIT_TO_CELSIUS_FACTOR 
FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9
global CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 
user = int(input("Enter the temperature to convert:"))
usertwo = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def  convert_to_celsius():
    celsius = (user-32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{user}°F is ",celsius,"°C")
    

def convert_to_fahrenheit():
   fahrenheit = user * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
   print(f"{user}°C is ",fahrenheit,"°F")


if usertwo == "F":
   convert_to_fahrenheit()
elif usertwo == "C":
    convert_to_celsius()
else :
    print('Invalid temperature. Please enter a numeric value.')