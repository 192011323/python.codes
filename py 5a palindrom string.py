str=str(input("enter a string:"))
r=reversed(str)
if(list(str)==list(r)):
    print('it is a palindrome')
else:
    print('it is not a palindrome')
