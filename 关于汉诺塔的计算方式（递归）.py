def hannoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hannoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上
        hannoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
n = int(input('请输入汉诺塔的层数：'))
hannoi(n,'第一根','第二根','第三根')
