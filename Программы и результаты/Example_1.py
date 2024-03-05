#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Если file2.txt сущесвует, то открыть его в режиме перезаписи, иначе - создать.
    fileptr = open("file2.txt", "w")
    # Запись данных в файл.
    fileptr.write(
        "Python is the modern day language. It makes things so simple.\nIt is the fastest-growing programing language")
    fileptr.close()  # Закрытие файла file2.txt
