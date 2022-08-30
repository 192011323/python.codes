lowerlimit=int(input("enter a lower limit:"))
upperlimit=int(input("enter a upper limit:"))
List = []
for n in range(lowerlimit,upperlimit+1):
    if((int(n**0.5))**2==n and sum(list(map(int,str(n))))<10):
        List.append(n)

print("the perfect squares numbers list which is less than 10:",List)
    
    
