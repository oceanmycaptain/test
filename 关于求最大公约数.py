def gcd(x,y):
    while y:#辗转相除法
        t=x%y
        x=y
        y=t
    return x
print((gcd(4,6)))#用于检验gcd函数结果
