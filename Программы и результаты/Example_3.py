#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Первый способ.
    # Если file2.txt сущесвует, то открыть его в режиме чтения, иначе - ошибка.
    fileptr = open("file2.txt", "r")
    # Запись данных из файла построчно в переменные.
    content1 = fileptr.readline()
    content2 = fileptr.readline()
    # Вывод строк файла.
    print(content1)
    print(content2)
    fileptr.close()  # Закрытие файла file2.txt

    # Второй способ.
    # Открытие файла в режиме чтения.
    # with open("file2.txt", "r") as fileptr:
    #    # Запись данных из файла построчно в переменные.
    #    content1 = fileptr.readline()
    #    content2 = fileptr.readline()
    #    # Вывод строк файла.
    #    print(content1)
    #    print(content2)
