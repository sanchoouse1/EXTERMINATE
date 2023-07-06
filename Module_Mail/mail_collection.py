import sqlite3 as sq

db = sq.connect('mails_collection_database.db')
cur = db.cursor()

async def db_start():
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS users("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "login TEXT, "
                    "password TEXT)")
        db.commit()
        print('[+] Успешное подключение к базе данных')
    except:
        print('[-] Ошибка подключения к базе данных')

async def add_module(login_, password_):
    try:
        cur.execute("SELECT login FROM users")
        cur.execute(f"INSERT INTO users(login, password) VALUES (?,?)", (login_, password_))
        db.commit()
        print(f'[+] Пользователь {login_} добавлен!')
    except:
        print(f'[-] Ошибка добавления пользователя.')

def get_my_login(ID_):
    try:
        login = cur.execute(f"SELECT login FROM users WHERE id = ?", (ID_, ))
        db.commit()
        result = login.fetchone()[0]
        return result
    except:
        print('[!] Произошла ошибка в модуле получения логина.')

def get_my_password(ID_):
    try:
        password = cur.execute(f"SELECT password FROM users WHERE id = ?", (ID_, ))
        db.commit()
        result_password = password.fetchone()[0]
        return result_password
    except:
        print('[!] Произошла ошибка в модуле получения пароля.')

async def show_all():
    try:
        cur.execute("SELECT login FROM users")
        db.commit
        result_all_show = cur.fetchall()
        for i in range(len(result_all_show)):
            print(result_all_show[i][0])      
    except:
        print('[!] Произошла ошибка при попытке показа всех пользователей.')

async def delete_all():
    try:
        cur.execute("DELETE FROM users")
        db.commit()
        db.close()
        print('[~] База данных очищена')
    except:
        print('[!] Ошибка в очистке базы данных.')


