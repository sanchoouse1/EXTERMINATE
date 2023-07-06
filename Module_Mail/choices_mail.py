import asyncio
from Module_Mail.attacking import *
from Module_Mail.mail_collection import *
from validate_email import validate_email
from Module_Mail.mail_change import change
from Module_Mail.adding_user import new_user

def choice_mail():
    try:
        victim_mail = open('Module_Mail/mail.txt')
        content_victim_mail = victim_mail.read()
        victim_mail.close()
    except:
        print('[!] Произошла ошибка открытия или чтения файла.')
    mail_answer = int(input(f'В файле почты находится адрес {content_victim_mail}\n0 — Атаковать\n1 — Изменить\n2 — Настройки\n>> '))
    match mail_answer:
        case 0:
            number_of_attacks = int(input("Укажите число сообщений которое будет отправленно с каждой почты >> "))
            asyncio.run(send_start(number_of_attacks))
        case 1:
            change()
        case 2:
            answer_about_changes = int(input("0 — Ввести новую почту\n1 — Вывести все данные\n2 — Удалить все\n>> "))
            match answer_about_changes:
                case 0:
                    new_user()
                case 1:
                    asyncio.run(show_all())
                case 2:
                    asyncio.run(delete_all())



if __name__=='__main__':
    choice_mail()

