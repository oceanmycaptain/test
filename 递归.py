def a(n):
    if n==1:
        return 1
    else :
        return n*a(n-1)

number = int(input('请输入一个正整数：'))
b = a(number)
print('%d的阶乘是：%d'%(number,b))
