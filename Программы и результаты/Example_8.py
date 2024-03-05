#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Открытие файла в режиме чтения.
    with open("file2.txt", "r") as fileptr:
        # Указатель сейчас на 0 байте.
        print("The filepointer is at byte :", fileptr.tell())
        # Перемещение указаталея на 10 байт.
        fileptr.seek(10)
        # tell() выводит, на каком байте сейчас указатель.
        print("After reading, the filepointer is at:", fileptr.tell())
