def reverse(str):
    num=" "
    for i in str:
        num=i+num
    return num
str= str(input("enter a string:"))
print("original",str)
print("reversed string",reverse(str))
