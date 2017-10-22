import random
secret = random.randint(1,2)
print('-------------我爱鱼c工作室--------------')
temp = input("猜一下小甲鱼现在心里想的是哪个数字:\n")
guess = int(temp)
if guess == secret:
    print("卧槽，你是小甲鱼心里蛆虫吗？！")
    print("哼，猜中了也没有奖励！")
else:
    if guess > secret:
        print("哥，大了大了！！")
    else:
        print('哥，小啦小啦~~')
    i=0
    while i < 2:
        temp = input("哎呀，猜错了，请重新输入吧:\n")
        guess = int(temp)
        i=i+1
        if guess == secret:
            print("卧槽，你是小甲鱼心里蛆虫吗？！")
            print("哼，猜中了也没有奖励！")
        elif guess > secret:
            print("哥，大了大了！！")
        else:
            print('哥，小啦小啦~~')
print("游戏结束，不玩啦~")
