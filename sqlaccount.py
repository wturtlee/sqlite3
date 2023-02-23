import sqlite3

#菜單
def menu():
    print("帳號、密碼管理系統")
    print("---------------------")
    print("1- 新增帳號、密碼")
    print("2- 顯示帳號、密碼")
    print("3- 修改密碼")
    print("4- 刪除帳號、密碼")
    print("0- 離開程式")
    print("---------------------")
    print("")

#新增程式
def addaccount_data():
    name = input("請輸入欲新增的名字:")
    account = input("請輸入欲新增的帳號:")
    password = input("請輸入欲新增的密碼:")
    print()
    sql = """
    INSERT INTO account (name,account,password)
    VALUES ({},{},{});
    """.format(name,account,password)
    cursor.execute(sql)
    conn.commit()

#顯示程式
def showaccount_data():
    print("目前的帳戶如下")
    for i in records:
        print(i)
    pass
    print("")
    input("請輸入任意鍵返回:")
    print("")

#修改程式
def reaccount_data():
    row_id = input("請選擇欲修改的資料:")

    password = input("請輸入欲新增的密碼:")
    print()
    sql = """
    update account
    set password = {}
    where id ={};
    """.format(password,row_id)
    cursor.execute(sql)
    conn.commit()

#刪除程式
def delaccount_data():
    row_id = input("請選擇欲刪除的資料:")
    sql = """
    delete from account
    where id = {};
    """.format(row_id)
    cursor.execute(sql)
    conn.commit()

#主程式開始
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

while True:
    cursor.execute('SELECT * FROM `account`;')
    records = cursor.fetchall()
    menu()
    choice = int(input("請輸入您的選擇:"))
    print()
    if choice ==1:
        addaccount_data()
    elif choice == 2:
        showaccount_data()
    elif choice == 3:
        reaccount_data()
    elif choice == 4:
        delaccount_data()
    elif choice == 0:
        break    

cursor.close()
conn.close
