'''
    变量：能变化存储数据的量
'''
#记录了第一个衣服的详细信息
name1 = "裙子"
material = '棉'
quanlity1= 'A+'
price = 40
num1=4

#记录了第二个衣服的详细信息
name2="卫衣"
material2='麻'
quanlity2='B+'
price2 =50
num2=5

#记录了第三个衣服的详细信息
name3='衬衫'
material3='防水布'
quanlity3='A+'
price3=60
num3=7

#记录了第四个衣服的详细信息
name4='棉服'
material4='棉布'
price4=80
num4=8

#记录了第五个衣服的详细信息
name5='羽绒服'
material5='绒'
price5=100
num5=9


print('------------欢迎来到服装商城--------------')
print('服装名称       质量       价格       数量'  )
print('---------------------------------------')
print(name1,"   ",material,"     ",price,"     ",num1    )
print(name2,"   ",material2,"    ",price2,"    ",num2    )
print(name3,"   ",material3,"    ",price3,"    ",num3    )
print(name4,"   ",material4,"    ",price4,"    ",num4    )
print(name5,"   ",material5,"    ",price5,"    " ,num5   )
print('----------------------------------------------------')
print('总金额：',(price * num1 +price2 * num2+ price3 * num3+ price4 * num4 + price5 * num5),'￥' )
















