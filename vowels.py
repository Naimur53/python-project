# 5、Character Counter vowels 


s = input("please enter some test :")
idx = 0
s_len = len(s)
number = 0
while idx < s_len:
    if s[idx] in "aAeEiIoOuU" :
        number = number + 1
        
    idx = idx + 1
print("number of vowels :", number)        