num1 = float(input("Please input a number: "))
num2 = float(input("Please input a second number: "))

operation = input("Choose operation (+, -, *, /)")

if operation == "+":
 result = num1+num2

elif operation == "-":
 result = num1-num2

elif operation == "*":
 result = num1*num2
 
elif operation == "/":
 if num2 != 0:
  result = num1/num2
 else:
  result = "Invalid Operation"  

print ("Result:", result)
