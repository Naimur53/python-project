# 6、Fibonacci Sequence 


n = int(input("please enter n :"))

n1 = 1
n2 = 1

# n1, n2 = 1,1

print(n1, end = ',')
while n2 < n :
    print(n2, end = ',')
    n1 = n2
    n2 = n1+n2
    
    # n1 , n2 = n2 , n1+n2

print("program has ended!")
