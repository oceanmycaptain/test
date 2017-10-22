num=10
print("猜猜我想的数字：")
a=int(input())
if a>num:
    print("数字太大了吧！")
    print("游戏结束。")
if a<num:
    print("数字太小了吧！")
    print("游戏结束")
if a==num:
    print("恭喜你答对了。")
