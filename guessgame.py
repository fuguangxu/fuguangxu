import random
import  time
num=random.randint(1,100)
counter=0  #计数器
while True: #一直执行循环
    if counter>=3:
        print ("输出三次没猜中，系统锁定5秒")
        f=1
        while f <= 5:
            print(".",end="")
            time.sleep (1) #睡眠一秒
            f=f+1
    counter=counter+1
    n=input("请输入您要猜的数字:")
    n=int(n)
    if n > num:
        print("大了!")
    elif n < num:
        print("小了！")
    else:
        print("恭喜您，猜对了！您本次猜了：",counter,"次！")
        break # 跳出循环体



