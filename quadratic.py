# 3 Solve a quadratic equation in Python 
# A quadratic equation has the form

import math

a = float(input("Enter the coefficient a :"))
b = float(input("Enter the coefficient b :"))
c = float(input("Enter the constant c :"))


# calculater the discriminant

discriminat = b** - 4*a*c

# check if the discriminant is positive, zero or negative

if discriminat > 0:
    x1 = (-b + math.sqrt(discriminat)) / (2*a)
    x2 = (-b - math.sqrt(discriminat)) / (2*a)
    print(f"the solutions are  : x1 = {x1}, x2 = {x2}")
elif discriminat ==0:
    x = -b / (2*a)
    print(f"the solution is: x = {x}")

else:
    print("the equation has no real solutions")
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminat)/ (2*a)
    print(f"the comples solution are : x1 = {real_part} +{imaginary_part}i, x2 = {real_part} - {imaginary_part}i")