'''
# 导入pymysql 增加
import pymysql
# 通过pymysql获取连接
con = pymysql.connect(host="localhost",user="root",password="" ,database="company")
# 获取游标
cursor = con.cursor() # 获取一个游标

# 准备一条sql语句
sql = "insert into t_dept values('90','炊事班','北京')"

# 执行sql语句
num = cursor.execute(sql)

print("影响了",num,"行数据")
# 提交实际数据
con.commit()  # 将缓存的数据真正的提交给数据库

# 关闭资源
'''
'''
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql="insert into t_employees values(%s,%s,%s,%s,%s,%s,%s,%s)"
param=["7991","小亮","销售员","7489","1981-3-26",4500,500,10]

num=cursor.execute(sql,param)
print("影响了",num,"行数据")
con.commit()

cursor.close()
con.close()
'''
#删除
'''
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql="delete from t_employees where ename=%s"
param=["小亮"]

num=cursor.execute(sql,param)
print("影响了",num,"行数据")
con.commit()

cursor.close()
con.close()
'''
#更新
'''
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql="update t_employees set sal =sal+100 where ename=%s"
param=["小付"]

num=cursor.execute(sql,param)
print("影响了",num,"行数据")
con.commit()

cursor.close()
con.close()
'''
#查询
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql="select * from t_employees where ename=%s"
param=["曹操"]
num=cursor.execute(sql,param)
data=cursor.fetchall()
print("影响了",num,"行数据")
con.commit()

cursor.close()
con.close()
print(data)




















