num1 = int(input())# first number is given input
num2 = int(input())#second number is given input 
operator = input()[0]


if operator == '+':
  print(num1 + num2)
elif operator == '-':
  print(num1 - num2)
elif operator == '*':
  print(num1 * num2)
elif operator == '/':
  print(num1 // num2)
else:
  print("Invalid operator")


