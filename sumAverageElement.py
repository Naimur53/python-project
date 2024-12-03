# 7、Sum  and average  of Elements 


n = int(input("Please enter the number of numbers to be summed :"))

s = 0

for i in range(1, n+1):
    number = float(input(f'enter the {i}th number :'))
    s += number
    
print(f'the sum is {s}')