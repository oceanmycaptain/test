count = 3
password ='hhh123'
while count:
    passwd = input('请输入密码：')
    count=count-1
    #此时的count每次输入一次就会减少一次。
    if passwd==password:
        print('密码正确，进入程序。')
        break
    elif '*' in passwd:
        count=count+1
#此时的count因为在上一次的运行时已经减少一次，这次运行时我们得把这次的机会再分享给用户。
        print('密码不能含有‘*’号！你还有',count,'次机会',end=' ')
        continue
