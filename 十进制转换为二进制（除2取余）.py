def Dec2Bin(dec):
    temp = []
    result = ''#最后打出来以字符的方式。
    while dec:
        quo = dec %2#用于判断余数
        dec =dec //2#地板式除法来得到下次我们需要的数字。
        temp.append(quo)
    while temp:
        #判断是否除尽2，除尽时会（while 0）不会再进行下一步。
        result +=str(temp.pop())
    return result
print(Dec2Bin(30))
