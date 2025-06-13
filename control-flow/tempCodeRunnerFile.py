num1  = input('Enter the first number:') 
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+" :
       print(f"{num1} + {num2} = {num1 + num2 }")
