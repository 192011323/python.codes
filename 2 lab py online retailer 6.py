a=int(input())
def cost(x):
    if a<1:
        print("enter a valid number")
    elif x==1:
        print(750)
    else:
        print(750+(x-1)*200)
cost(a)
