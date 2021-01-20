'''
    print()  打印的方法，可以将你想要打印的数据写到print方法里
'''
# 记录了第一个水果详细信息
name1 = "砂糖橘子"
price1 = 6
quanlity1 = 'A+'
num1 = 25
unit1 = '个'

# 记录了第二个水果详细信息
name2 = "苹果"
price2 = 3
quanlity2 = 'C+'
num2 = 10
unit2 = '个'

# 记录了第三个水果的详细信息
name3="芒果"
price3=5
quanlity3='B+'
num3=4
unit3='个'

#记录了第四个水果的详细信息
name4="西瓜"
price4=6
quanlity4='c+'
num4=6
unit4='个'

#记录了第五个水果的详细信息
name5="草莓"
price5=6
quanlity5='A+'
num5=7
unit5='个'


print('-----------------欢迎来到水果商城--------------------')
print('水果名称         价格        品质        数量     单位')
print('----------------------------------------------------')
print(name1,"    ",price1,"    ",quanlity1,"    ",num1,"    ",unit1)
print(name2,"    ",price2,"    ",quanlity2,"    ",num2,"    ",unit2)
print(name4,"    ",price4,"    ",quanlity4,"    ",num4,"    ",unit4)
print(name5,"    ",price5,"    ",quanlity5,"    ",num5,"     ",unit5)
print('-----------------------------------------------------')
print(' 总金额为：',(price1 * num1 + price2 * num2 +price3 * num3 +price4 * num4 + price5* num5),'￥')
















