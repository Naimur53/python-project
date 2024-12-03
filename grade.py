# 1、Write a program that takes a score (0-100) as
# input and outputs the corresponding letter grade:

score = int(input("inter your score : "))

if score >= 90:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade : D")
    
else:
    print("Grade: F")