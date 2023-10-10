# -*- coding: utf-8 -*-

import sys


class Memory:
    # Инициализация переменных
    def __init__(self, char):
        self.char = char

    # Свойство класса - подсчет символов в байтах
    def byte_size(self):
        return sys.getsizeof(self.char)

    # Свойство класса - подсчет сиволов в битах
    def bit_size(self):
        return sys.getsizeof(self.char) * 8


def input_char():
    while True:
        char = input('Введите символы для подсчета их битов и байтов: ')
        if not char:        # Пустая строка, выход с цикла
            break

        mem = Memory(char)
        byte = mem.byte_size()
        bit = mem.bit_size()
        
        print(f'Биты: {bit}\
             \nБайты: {byte}')
    
input_char()