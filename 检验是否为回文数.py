print('请输入一个数字：')
a=str(input())
if a[::-1]==a:
    print('该数字为回文数：',a)
else:
    print('该数字不是回文数字')
    
