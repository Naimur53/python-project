# number = int(input("enter a number :"))
# for number in range(100,1000):
#     a = number // 100
#     c = number % 10
#     b = number % 100 // 10
    
#     if (a** + b** c**3) == number:
#         print(f"{number}",end=" ")

def is_daffodil_number (num):
    
        number = num // 100
        tens =(num //10)%10
        ones = num %10
        return num ==(number**3 + tens**3 + ones**3)
daffodilNumber = []
for number in range(100,1000):
    if is_daffodil_number(number):
        daffodilNumber.append(number)
print("Daffodil numbers (Armstrong numbers) between 100 and 999 are:", daffodilNumber)