def change():
    try:
        file = open('Module_Mail/mail.txt', 'w')
        print('[!] Вы открыли файл с почтой.')
        chan_ge = input('Введите новую почту >> ')
        file.write(chan_ge)
        file.close()
    except:
        print('[!] Ошибка открытия и записи в файл почты.')