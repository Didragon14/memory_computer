# -*- coding: utf-8 -*- 

# Мой первый репозиторий)) через git
# Пробую все эти плющки с git add 'name file';  git status и т.д.

def memory_computer():
    begin = int(input('Добро пожаловать, введите 1 чтобы начать 0 чтобы не начинать: '))
    
    if begin == 1:
        while begin != 0:

            word = input('\nВведите символы для определения объёма памяти: ')

            # Биты
            bits = len(word) * 8
            # Байты
            bytes = bits // 8
            print(f'\nВ символах {word} \nБиты: {bits} \nБайты: {bytes} ')
            print('\nДля прекращения программы напишите: 0')

            # Конец программы
            if word in '0':
                break
    else:
        print('До свидания! ')

memory_computer()