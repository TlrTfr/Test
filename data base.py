import sqlite3
from random import randint

#Делаем переменные глобальными.
global data
global cur

#Создаем базу данных. base - название.
data = sqlite3.connect("base.data")
#Создаем курсор.
cur = data.cursor()

#Создание таблицы.
#CREATE TABLE IF NOT EXISTS users - создать столбец если такого нет.
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    Login TEXT,
    Password TEXT,
    Age BIGINT,
    Cash INT
)""")

#Подтверждение создания таблицы.
data.commit()

def reg():
    #Спрашиваем логин и пароль
    user_Login = input("Login : ")
    user_Passwoed = input ("Password : ")
    user_Age = input("Age : ")
    #SELECT Login FROM users - Выбрать атрибут Login в таблице users.
    #WHERE Login = '{user_Login}' - Проверяет наличие логина. если такой логин имеется, действeет else.
    cur.execute(f"SELECT Login FROM users WHERE Login = '{user_Login}'")
    if cur.fetchone() is None:
        #fetchone - выбрать одно, fetchall - выбрать все
        cur.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (user_Login, user_Passwoed, user_Age, 0))
        #Подтверждаем добавление в базу данных.
        data.commit()

        print("Данные добавлены в базу данных")
    else:
        print("Такие данные уже есть")

        for value in cur.execute("SELECT * FROM users"):
            print(value)

def delete_data():
    #DELETE Login FROM users WHERE Login - удалить атрибут Login в таблице users
    cur.execute(f'DELETE FROM users WHERE Login = "{user_Login}"')
    data.commit()

    print("Данные удалены")

def casino():
    global user_Login
    user_Login = input("Log in : ")
    user_Password = input("Pass in : ")
    num = randint(1, 2)

    for i in cur.execute(f"SELECT Cash FROM users WHERE Login = '{user_Login}'"):
        balance = i[0]

    #SELECT Login FROM users WHERE Login = "{user_Login}" - Звучит как выбрать стобец Login в таблице users
    #Где логин "{user_Login}"
    cur.execute(f'SELECT Login FROM users WHERE Login = "{user_Login}"')
    #Если такого логина нет, перекидываем на функцию регистрации.
    if cur.fetchone() is None:
        print("Таких данных нет в базе данных, зарегистрируйтесь ")
        reg()
    else:
        if num == 1:
            #UPDATE - обновить, SET - добавить
            cur.execute(f'UPDATE users SET cash = "{10 + balance}" WHERE Login = "{user_Login}"')
            data.commit()
        else:
            #если пользователь проиграет, его данные удаляются.
            print("!!!You Lose!!!")
            delete_data()

def enter():
    for i in cur.execute('SELECT Login, Cash FROM users'):
        print(i)
def main():
    casino()
    enter()

main()
