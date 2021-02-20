import  pymysql
host="localhost"
database="六大首富"
user="root"
password=""
def update(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.executemany(sql,param)
    con.commit()
    cursor.close()
    con.close()
def find(sql,param,mode="all",size=1):
    con=pymysql.connect(host=host, user=user, password=password, database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    if mode=="all":
        return cursor.fetchall()
    elif mode=="one":
        return  cursor.fetchone()
    elif mode=="many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()
# sql="insert into money values(%s,%s,%s)"
# param=[["贾生",47,500000],
#        ["马云",58,1000000],
#        ["马化腾",57,1000202],
#        ["付光旭",20,560300004],
#        ["穆子康",24,230023],
#        ["杜会朦",25,204892]]
# update(sql,param)

sql="select 资产 from money "
param=[]
date=find(sql,param,mode="all",size=6)
print(date)
s=0
for i in date:
    s=s+sum(i)
print(s)





