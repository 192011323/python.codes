def check(st1,st2):
    if(sorted(st1)==sorted(st2)):
        print('the strings are anagram')
    else:
        print('the strings are not anagram')
st1=str(input("enter a word:"))
st2=str(input("enter another word:"))
check(st1,st2)
