#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Первый способ.
    # Если newfile.txt сущесвует, то ошибка, иначе - создать.
    fileptr = open("newfile.txt", "x")
    print(fileptr)
    if fileptr:
        print("File created successfully.")
    # Закрытие файла.
    fileptr.close()

    # Второй способ.
    # Создание файла, если такого ещё не существует.
    # with open("newfile.txt", "x") as fileptr:
    #    print(fileptr)
    #    if fileptr:
    #       print("File created successfully")
