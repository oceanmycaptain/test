i=0
string='ILoveFishC.com'
length=len(string)
#此时直接用len（string）与i比较时，会每次测量string长度，效率会变得相当低
while i<length:
    print(i)
    i+=1
