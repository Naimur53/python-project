
# 2、Write a Python program that takes two numbers and an operator (+, -, *, /)
# as input and performs the corresponding operation

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
operator = (input("enter operator(+,-,*,/) :"))



if operator == '+' :
    print(f"Result : {num1 + num2}")
    
elif operator == '-' :
    print(f"Result : {num1 - num2}")
    
elif operator == '/' :
    if num2 != 0:
         print(f"Result : {num1 / num2}")
    else:
        print("cannot divide by zero")
    
elif operator == '*' :
    print(f"Result : {num1 * num2}")
    
else:
    print("invalid operator")
    

    
