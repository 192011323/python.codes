def add(m,n):
    return(m+n)
def sub(m,n):
    return(m-n)
def mul(m,n):
    return(m*n)
def div(m,n):
    return(m/n)
print("enter a choice:")
print("1. addition)")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter choice 1/2/3/4:")
    if choice in ('1','2','3','4',):
        m=float (input("enter the first number:"))
        n=float (input("enter the second number:"))
        if(choice=='1'):
            print('addition',add(m,n))
        elif(choice=='2'):
            print('sub',sub(m,n))
        elif(choice=='3'):
            print('mul',mul(m,n))
        elif(choice=='4'):
            print('div',div(m,n))
    else:
        print('the operation does not exist!')
        
        
     
