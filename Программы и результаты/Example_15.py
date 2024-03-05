#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    # Работа с аргументами(sys.argv. На 0 месте стоит имя файла), переданными программе в командной строке.
    print("Number of arguments:", len(sys.argv), "arguments")
    print("Argument List:", str(sys.argv))
