def factorial(n):#先定义一个函数
    result = n
    for i in range(1,n):
        result *=i
    return result
number = int(input('请输入一个正整数：'))
a = factorial(number)
print('%d的阶乘是：%d'%(number,a))
