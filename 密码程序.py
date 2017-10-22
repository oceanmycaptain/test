print('请输入密码：')
a=123
b=int(input())
c=1
if b==a:
    print('密码正确！')
while a!=b and c!=3:
    print('密码错误请重新输入：')
    b=int(input())
    c+=1
if c==3 and a==b:
    print('密码正确')
    
