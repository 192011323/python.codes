n = int(input("enter the number"))
a=str(input("enter a character"))
for i in range(1, n+1):
    # internal loop run for i times
    for k in range(1, i+1):
        print(a, end="")
    print()
