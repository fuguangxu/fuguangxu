# class Cup:
#     __high=0
#     __v=0
#     __color=""
#     __tom=""
#     def setHigh(self,high):
#         self.__high=high
#     def getHigh(self):
#         return self.__high
#
#     def setV(self,v):
#         self.__v=v
#     def getV(self):
#         return self.__v
#
#     def setColor(self,color):
#         self.__color=color
#     def getColor(self):
#         return self.__color
#
#     def setTom(self,tom):
#         self.__tom=tom
#     def getTom(self):
#         return self.__tom
#
#     def save(self,much):
#         if much>self.__v:
#             print("水冒了！")
#         else:
#             print('这杯水可存放',much,"毫升水")
# p=Cup()
# p.setHigh(5)
# p.setV(1000)
# p.setColor("蓝色")
# p.setTom("玻璃")
# print("这个杯子的材质是",p.getTom(),"容积为",p.getV(),"ml","颜色为",p.getColor(),"高度为",p.getHigh(),"cm")
# p.save(1200)

class Computer:
    __size=""
    __price=0
    __cpu=0
    __meory=0
    __open=""
    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setOpen(self,open):
        self.__open=open
    def getOpen(self):
        return self.__open

    def setMeory(self,meory):
        self.__meory=meory
    def getMeory(self):
        return self.__meory

    def dazi(self):
        print("笔记本正在打字")
    def playgames(self):
        print("笔记本正在打游戏")
    def seetv(self):
        print("笔记本正在看视频")
p=Computer()
p.setPrice(5000)
p.setCpu(8)
p.setMeory(8)
p.setSize(12)
p.setOpen(2)
print("这台电脑的价格是",p.getPrice(),"元","内存大小为",p.getMeory(),"G","cpu内存大小为",p.getCpu(),"尺寸为",
      p.getSize(),"英寸","待机时长为",p.getOpen(),"小时")

p.playgames()
p.dazi()
p.seetv()
















