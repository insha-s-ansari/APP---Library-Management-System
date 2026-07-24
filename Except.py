try:
    a=int(input("enter any num:"))
    b=int(input("enter any num:"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divided bu zero")
