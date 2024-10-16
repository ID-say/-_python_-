# 导入pymysql库
import time

import pymysql.err
from pymysql import Connection
conn = Connection(
    host="localhost",       # 主机名(IP)
    port=3306,              # 端口
    user="root",            # 账户
    password="it006126",    # 密码
    autocommit=True         # 【可选】设置自动提交\自动commit\自动确认
)

new_cursor = conn.cursor()
conn.select_db("userdata")
# 创建用户信息表
try:
    new_cursor.execute("CREATE TABLE account_data( 姓名 VARCHAR(3), 身份证号码 varchar(18), 电话号码 varchar(11),密码 varchar(6));")
except pymysql.err.OperationalError:
    print("用户信息表已存在，无需创建表")
# 用户注册
def userRegistration():
    name = input("请输入您的姓名：")
    id_num = int(input("请输入您的18位身份证号码："))
    telephoneNumber = int(input("请输入您的11位电话号码："))
    password = int(input("请设置您的6位数字密码："))
    new_cursor.execute(f"INSERT INTO account_data(姓名,身份证号码,电话号码,密码) VALUES('{name}',{id_num},{telephoneNumber},'{password}');")
# 用户登录
new_cursor.execute("select 姓名 from account_data;")
a = new_cursor.fetchall()[0][0]     # 获取数据库账号
new_cursor.execute("select 密码 from account_data;")       # 获取数据库密码
b = new_cursor.fetchall()[0][0]
new_cursor.execute("select * from account_data")
c = new_cursor.fetchall()

account_list = []       # 账号列表
password_list = []      # 密码列表
for x in c:
    # print(x)
    account_list.append(x[0])
# print(account_list)
for y in c:
    password_list.append(y[-1])
# print(password_list)

def userLogin():
    num = 0
    while True:
        name = input("请输入姓名：")
        if account_list.count(name) == 1:
            print("账号存在，请输入密码")
            while True:
                subscript = account_list.index(name)    # 获取到文件下标
                if password_list[subscript] == input("密码："):
                    thatSRight = True
                    print("密码正确")
                    return True
                    break
                else:
                    print("密码错误")
            break
        else:
            if num != 2:
                print("账号不存在")
                num+=1
            else:
                print("错误次数过多！！！")
                break


# 疫苗信息管理
# 创建疫苗信息表
try:
    new_cursor.execute("CREATE TABLE vaccine_data( 疫苗名称 VARCHAR(4), 生产厂家 varchar(9), 有效期 date,疫苗id int);")
except pymysql.err.OperationalError:
    print("疫苗信息表已存在，无需创建表")
# 添加疫苗信息
def addVaccineInformation():
    while True:
        account_input = input("请输入管理员账号：")
        password_input = input("请输入管理员密码：")
        new_cursor.execute("select * from administrator_data;")
        accountPassword = new_cursor.fetchall()[0]
        if accountPassword[0] == account_input:
            print("账号正确")
            if accountPassword[1] == password_input:
                print("密码正确")
                theNameOfTheVaccine = input("请输入疫苗名称：")
                manufacturer = input("请输入生产厂家：")
                expirationDate = input("请输入有效期：")
                quantity = input("请输入疫苗id：")
                new_cursor.execute(f"INSERT INTO vaccine_data(疫苗名称,生产厂家,有效期,疫苗id) VALUES('{theNameOfTheVaccine}','{manufacturer}','{expirationDate}',{quantity});")
            else:
                print("密码错误")
                time.sleep(3)
                break
        else:
            print("账号错误")
            time.sleep(3)
            break
# 疫苗查询
new_cursor.execute("select * from vaccine_data")
d = new_cursor.fetchall()

id_list =[]
for x in d:
    id = x[-1]
    id_list.append(id)
print(id_list)
# 查询
def vaccineInquiry():
    number = 0
    while number != 2:
        try:
            id_01 = id_list.index(int(input("请输入需要查询的疫苗id：")))
            print(f"疫苗信息为：{d[id_01]}")
            break
        except ValueError:
            print("目标不存在")
            number+=1


# 预约接种
# 获取接种信息
def a():
    a_01 = "疫苗种类01"
    a_02 = "疫苗种类02"
    a_03 = "疫苗种类03"
    abc = int(input("请选择你要预约接种的疫苗种类："))
    if abc == 1:
        print(a_01)
        return a_01
    elif abc == 2:
        print(a_02)
        return a_02
    elif abc == 3:
        print(a_03)
        return a_03
    else:
        print("请输入正确的选项")

def b():
    b_01 = "接种时间01"
    b_02 = "接种时间02"
    b_03 = "接种时间03"
    cde = int(input("请选择你要预约接种的接种时间："))
    if cde == 1:
        print(b_01)
        return b_01
    elif cde == 2:
        print(b_02)
        return b_02
    elif cde == 3:
        print(b_03)
        return b_03
    else:
        print("请输入正确的选项")

def c():
    c_01 = "接种地点01"
    c_02 = "接种地点02"
    c_03 = "接种地点03"
    efg = int(input("请选择你要预约接种的接种地点："))
    if efg == 1:
        print(c_01)
        return c_01
    elif efg == 2:
        print(c_02)
        return c_02
    elif efg == 3:
        print(c_03)
        return c_03
    else:
        print("请输入正确的选项")



# 创建预约接种信息表
try:
    new_cursor.execute("CREATE TABLE revise_data( 疫苗种类 VARCHAR(6), 接种时间 varchar(6), 接种地点 varchar(6));")
except pymysql.err.OperationalError:
    print("接种信息表已存在，无需创建")



# 添加数据至MySQL
def makeAnAppointmentForVaccination():
    new_cursor.execute(f"INSERT INTO revise_data(疫苗种类,接种时间,接种地点) VALUES('{str(a())}','{str(b())}','{str(c())}');")

# 预约查询
def inquire_data():
    a_01 = "疫苗种类01"
    a_02 = "疫苗种类02"
    a_03 = "疫苗种类03"
    abc = int(input("请选择你要查询疫苗种类："))
    if abc == 1:
        print(a_01)
        return a_01
    elif abc == 2:
        print(a_02)
        return a_02
    elif abc == 3:
        print(a_03)
        return a_03
    else:
        print("请输入正确的选项")

def appointmentEnquiry():
    new_cursor.execute(f"select * from revise_data where 疫苗种类 = '{str(inquire_data())}';")
    e = new_cursor.fetchall()
    print(f"查询到的信息为：{e}")

# 预约修改                                             修改哪一列   修改为啥内容        判断用来更新指定行
def appointmentModifications():
    try:
        new_cursor.execute("UPDATE revise_data SET `疫苗种类1` = '疫苗种类02' WHERE `疫苗种类` = '疫苗种类03';")
        print("修改成功！！！")
    except:
        print("所需要修改的信息不存在")

# 接种记录
# 创建接种信息表（自动记录——数据自动获取，无需用户输入）
try:
    new_cursor.execute("CREATE TABLE inoculation_data ( 疫苗种类 varchar(6), 接种日期 varchar(6),接种地点 varchar(6));")
except pymysql.err.OperationalError:
    print("接种信息表已存在，无需创建表")

# 自动获取接种信息
def getVaccinationInformation():
    new_cursor.execute("select * from revise_data;")
    g = new_cursor.fetchall()
    print(g)
    # 添加信息到MySQL中
    for x in g:
        new_cursor.execute(f"INSERT INTO inoculation_data(疫苗种类,接种日期,接种地点) VALUES('{str(x[0])}','{str(x[1])}','{str(x[2])}');")

# 接种查询
def vaccinationInquiry():
    new_cursor.execute(f"select * from inoculation_data where 疫苗种类 = '{str(inquire_data())}';")
    h = new_cursor.fetchall()
    print(f"查询到的信息为：{h}")


# 系统管理

# 创建管理员信息表
try:
    new_cursor.execute("CREATE TABLE administrator_data ( 账号 varchar(11), 密码 varchar(8));")
except pymysql.err.OperationalError:
    print("管理员信息表已存在，无需创建表")

# 添加管理员身份信息
def add_admin_data():
    new_cursor.execute(f"INSERT INTO administrator_data(账号,密码) VALUES('{input('请输入管理员账号')}','{input('请输入管理员密码')}');")


# 主菜单

Login = "未登录"
while True:
    print("------主菜单------")
    print("用户注册\t\t1")
    print("用户登录\t\t2")
    print("添加疫苗信息\t3")
    print("疫苗信息查询\t4")
    print("添加接种记录\t5")
    print("预约查询\t\t6")
    print("预约修改\t\t7")
    print("获取接种信息\t8")
    print("接种证明\t\t9")
    print("退出exit\t\t10或任意键")
    function = int(input("请输入你要选择的功能:"))
    if function == 1:
        userRegistration()
    elif function == 2:
        userLogin()
    elif function == 3:
        addVaccineInformation()
    elif function == 4:
        vaccineInquiry()
        time.sleep(2)
    elif function == 5:
        makeAnAppointmentForVaccination()
        time.sleep(2)
    elif function == 6:
        appointmentEnquiry()
        time.sleep(2)
    elif function == 7:
        appointmentModifications()
        time.sleep(2)
    elif function == 8:
        getVaccinationInformation()
        time.sleep(2)
    elif function == 9:
        vaccinationInquiry()
        time.sleep(2)
    elif function == 10:
        break
    else:
        break