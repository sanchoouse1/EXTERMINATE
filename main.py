import asyncio
from os import system
from Module_Mail.mail_collection import db_start
from Module_Mail.choices_mail import choice_mail


def logo():
    system("mode con cols=99 lines=30")
    print("""
——————————————————————————————————————————————————————————————————————————————————————————————————
######## ##     ## ######## ######## ########  ##     ## #### ##    ##    ###    ######## ######## 
##        ##   ##     ##    ##       ##     ## ###   ###  ##  ###   ##   ## ##      ##    ##       
##         ## ##      ##    ##       ##     ## #### ####  ##  ####  ##  ##   ##     ##    ##       
######      ###       ##    ######   ########  ## ### ##  ##  ## ## ## ##     ##    ##    ######   
##         ## ##      ##    ##       ##   ##   ##     ##  ##  ##  #### #########    ##    ##       
##        ##   ##     ##    ##       ##    ##  ##     ##  ##  ##   ### ##     ##    ##    ##       
######## ##     ##    ##    ######## ##     ## ##     ## #### ##    ## ##     ##    ##    ########\n
——————————————————————————————————————————————————————————————————————————————————————————————————\n\t\t\t\t\t\t\t\t\t    © 03.07.2023 0U751D312\n
0 — Mail        1 — Telegram        2 — What's App       3 — Вконтакте       4 — Комплексная атака
5 — Выход\n""")

def attack():
    attack_variant = int(input('Выберите вариант атаки >> '))
    match attack_variant:
        case 0:
            try:
                asyncio.run(db_start())
                choice_mail()
            except:
                pass
        case 1:
            try:
                pass
            except:
                pass
        case 2:
            try:
                pass
            except:
                pass
        case 3:
            try:
                pass
            except:
                pass
        case 4:
            try:
                pass
            except:
                pass
        case 5:
            quit()


def main():
    logo()
    attack()

if __name__=='__main__':
    main()