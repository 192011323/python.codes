def reverse(str):
    s=" "
    for i in str:
        s=i+s
    return s
str= str(input("enter a string:"))
print("original",str)
print("reversed string",reverse(str))
