#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":
    # Модуль OS изменяет текущий рабочий каталог, перейдя в C:\Windows.
    os.chdir("C:\\Windows")
    print(os.getcwd())
