#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    # Работа с аргументами(sys.argv. На 0 месте стоит имя файла), переданными программе в командной строке.
    for idx, arg in enumerate(sys.argv):
        print(f"Argument #{idx} is {arg}")
    print("Amount of arguments passed is ", len(sys.argv))
