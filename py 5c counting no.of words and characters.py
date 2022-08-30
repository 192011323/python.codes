s=str(input("enter the string:"))
char=0
word=1
for i in s:
    char=char+1
    if(i==' '):
        word=word+1
print('the no.of words in the string:',word)
print('the no.of charecters in the string:',char)
