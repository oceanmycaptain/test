def fab(n):
    if n<0:
        print('输入有误，请输入正整数！')
        return -1
    if n==1 or n==2:#此时就在给n==1和n==2进行赋值1
        return 1
    if n>2:
        return fab(n-1)+fab(n-2)#该处一直到fab（1）+fab（2）才开始停止。
s=fab(20)
if s>0:
    print('总共有%d对兔子'%s)
