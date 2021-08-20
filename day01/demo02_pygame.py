import random

print("#"*100)
print("1.开始游戏")
print("2.退出游戏")

while True:
    ch = input("等待选择:")  # 返回的是字符串类型
    if ch == "1":
        # 电脑出拳:
        computer = str(random.randint(1, 3))
        person = input("输入：剪刀：1、石头：2、布：3：")
        if computer == person:
            print("平局")
            pass
        elif computer == "1" and person == "2":
            print("你赢了，电脑剪刀，你石头")
            pass
        elif computer == "1" and person == "3":
            print("你输了，电脑剪刀，你布")
            pass
        elif computer == "2" and person == "1":
            print("你输了，电脑石头，你剪刀")
            pass
        elif computer == "2" and person == "3":
            print("你赢了，电脑石头，你布")
            pass
        elif computer == "3" and person == "1":
            print("你赢了，电脑布，你剪刀")
            pass
        elif computer == "3" and person == "2":
            print("你输了，电脑布，你石头")
            pass
        pass
    else:
        break
    pass