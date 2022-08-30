x= int(input("X="))
n= int(input("N="))
print("1.pow \n2.add\n3.sub\n4.mul\n5.div")
choice=int(input("choice:"))
if (choice==1):
    pow=x**n
    print(pow)
elif  (choice==2):
    add=x+n
    print(add)
elif (choice==3):
    sub=x-n
    print(sub)
elif (choice==4):
    mul=x*n
    print(mul)
elif (choice==5):
    div=x/n
    print(div)
else:
    print("invalid choice")
