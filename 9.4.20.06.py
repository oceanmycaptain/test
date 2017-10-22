import random
num=random.randint(1,10)
num=8
b=1
print("猜猜我想的数字")
a=int(input())
if a==num:
    print("第一次就猜对了，厉害啊！")
else:
while b!=3 and a!=num:
    if a==num:
        print("哈哈，猜对了")
    if a>num:
         print("数字大了，再来一次")
    if a<num:
         print("数字小了，再来一次")
    a=int(input())
    b+=1
while a==num and b==3:b
     print("最后一次猜对了")
while a!=num and b==3:
     print("最后一次也猜错了！")
print("游戏结束")
            
    
        
    
        

    
