#厨师
# class Cooker:
#     __name=None
#     __age=None
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name
#
#     def setAge(self,age):
#         self.__age=age
#     def getAge(self):
#         return self.__age
#
#     def cook1(self):#定义的蒸饭的方法
#         pass#无返回值
#
# class Cook2(Cooker):#定义cooker的子类
#     def chaocai(self):
#         pass
#
# class Cooker2_2(Cook2):#定义子类的子类（孙子类）
#     def chaocai(self):#重写父类的所有方法 chaocai和zhu
#         super().chaocai()
#         print(self.getName(),"正在炒菜")
#
#     def zhu(self):#煮调用的cook1里的无返回值的那个pass
#         super().cook1()#super就是父类，拥有父类里的所有东西
#         print(self.getName(),"正在煮饭")
#
# c=Cooker2_2()
# c.setName("小付")
# c.setAge("24")
# print(c.getName(),c.getAge())
# c.chaocai()#调用孙子类里面的2——2
# c.zhu()

#i.	人：年龄，性别，姓名。
#ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
#iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
class Person:
    __age=None
    __sex=None
    __name=None
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

class worker(Person):
    def wor(self,name,age,sex):
        super().setName(name)
        super().setAge(age)
        super().setSex(sex)
    def gongzuo(self):
        print(c.getName(),"正在工作")

class student(Person):
    __num=None
    def setNum(self,num):
        self.__num=num
    def getNum(self):
        return self.__num
    def wor(self,name,age,sex,num):
        super().setName(name)
        super().setAge(age)
        super().setSex(sex)
        self.__num = num
    def study(self):
        print(c.getName(),"正在学习")
    def song(self):
        print(c.getName(),"正在唱歌")


c=worker()
c.wor("xxxx","d","ddd")
print(c.getAge(),c.getSex(),c.getName())
c.gongzuo()

s=student()
s.wor("xxxx","d","ddd","gggggg")
print(s.getAge(),s.getSex(),s.getName(),s.getNum())
s.song()
s.study()




















