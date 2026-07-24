print("hello world!")
print() #---------------------------------------1
a=int(input("enter any number you want to add:"))#------------2
b=int(input("enter any number you want to add:"))
sum=a+b
print(sum)
print()
len=int(input("enter lenth:"))#-------------------------------3
width=int(input("enter width:"))
area=len*width
print(area)
print()
a=int(input("enter any number:"))#----------------------------4
b=int(input("enter any number:"))
a,b=b,a
print("the numbers are swaped:",a,b)
num=int(input("enter any number:"))#--------------------------5
if num%2==0:
    print("the number is even")
elif num<0:
    print("the num is negitive")
else:
    print("the number is odd ")
