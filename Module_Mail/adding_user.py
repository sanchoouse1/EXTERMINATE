import asyncio
from Module_Mail.mail_collection import add_module
from validate_email import validate_email

def new_user():
    try:
        answer_login = input('Укажите логин новой почты >> ')
        login_valid = validate_email(answer_login)
        if login_valid == True:
            answer_password = input('Введите пароль >> ')
            asyncio.run(add_module(answer_login, answer_password))
        elif login_valid == False:
            print(f'Адрес {answer_login} указан некорректно!\nСимволы (!#$%^&*"№;%:?*) не должны присутствовать в адресе.')
    except:
        print('[!] Ошибка авторизации нового пользователя.')
