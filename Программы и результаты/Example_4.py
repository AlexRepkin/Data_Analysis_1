#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Первый способ.
    # Если file2.txt сущесвует, то открыть его в режиме чтения, иначе - ошибка.
    fileptr = open("file2.txt", "r")
    # Запись сразу всех строк из файла в переменную.
    content = fileptr.readlines()
    # Вывод строк файла.
    print(content)
    fileptr.close()  # Закрытие файла file2.txt

    # Второй способ.
    # Открытие файла в режиме чтения.
    # with open("file2.txt", "r") as fileptr:
    #    # Запись сразу всех строк из файла в переменную.
    #    content = fileptr.readlines()
    #    # Вывод строк файла.
    #    print(content)
