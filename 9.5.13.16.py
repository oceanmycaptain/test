import random
num=random.randint(1,99)
b=1
print("猜猜我想的数字")
a=int(input())
if a==num:
    print("哈哈，第一次就猜对了")
else:
    while b!=8 and a!=num:
        if a>num:
            print("数字大了")
        if a<num:
            print("数字小了")
        a=int(input())
        b+=1
    if a!=num and b==8:
        print("最后一次猜错了，结束游戏")
    if a==num and b==8:
        print("最后一次猜对啦")
    if a==num and b!=8:
        print("哈哈，猜对了。")
print("游戏结束")
