#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Первый способ.
    # Если file2.txt сущесвует, то открыть его в режиме добавления информации в конец, иначе - создать.
    fileptr = open("file2.txt", "a")
    # Запись данных в файл.
    fileptr.write(" Python has an easy syntax and user-friendly interaction.")
    fileptr.close()  # Закрытие файла file2.txt

    # Второй способ.
    # Открытие файла в режиме добавления информации в конец.
    # with open("file2.txt", "a") as fileptr:
    #    # Добавление текста в конец файла.
    #    fileptr.write(
    #        " Python has an easy syntax and user-friendly interaction.")
