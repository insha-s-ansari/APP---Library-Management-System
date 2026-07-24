num=int(input("enter any number:"))#--------------------------1
if num<0:
    print("the number is negitive")
elif num>0:
    print("the num is positive")
else:
    print("the number is zero")

marks=int(input("enter marks:"))#----------------------------2
if marks>=91:
    print("outstanding")
elif marks>=81:
    print("A+")
elif marks>=71:
    print("B+")
else:
    print("failed")

word=input("enter any word:")#-------------------------------3
if word in "aeiou":
    print("vowels")
else:
    print("consonats")
