import random
import string
from pathlib import Path
import os

print('=== Генератор надёжных паролей ===')


while True:
    try:
        length = int(input('Введите длину пароля (длина пароля должна быть не менее 8 символов): '))
        if length >= 8:
            break
        else:
            print('Введите длину, большую либо равную 8')
    except ValueError:
        print('Ошибка, введите число!')

    
    

use_lower = input('Использовать ли строчные буквы? (да/нет): ').lower() == 'да'    
use_upper = input('Использовать ли заглавные буквы? (да/нет): ').lower() == 'да'
use_digits = input('Использовать ли цифры? (да/нет): ').lower() == 'да'
use_specials = input('Использовать ли спецсимволы? (да/нет): ').lower() == 'да'

chars = ''
if use_lower:
    chars += string.ascii_lowercase
if use_upper:
    chars += string.ascii_uppercase
if use_digits:
    chars += string.digits
if use_specials:
    chars += string.punctuation

if not chars:
    print('Не выбран ни один символ. Выход')
    exit()


password = ''.join(random.choice(chars)for _ in range(length))
print(f'Ваш пароль: {password}')

desktop_path = Path.home() / 'Desktop' 

if not desktop_path.exists():
    desktop_path = Path.home() / "Рабочий стол"

file_path = desktop_path / 'password.txt'


with open(file_path, 'a', encoding='utf-8') as file:
    if os.path.getsize(file_path) == 0:
        file.write(password)
    else:
        file.write('\n' + password)
    print('На рабочем столе создан файл "password" с вашим паролем. Если файл уже есть на рабочем столе, то добавлен в него.')

input('Нажмите Enter для выхода...')