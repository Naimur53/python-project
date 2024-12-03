number = int(input("please enter a number :"))

isPrime = True

for f in range(2,number):
    
    if number % f == 0:
        isPrime = False
        break
if isPrime :
     print(f"{number} is a prime number")
        
else:
     print(f"{number} is not a prime number")