def function(n):
    a=n
    for i in range(1,n):
        a*=i
    return a
n=int(input('请输入一个正整数：'))
b=function(n)
print('%d的阶乘是：%d'%(n,b))
