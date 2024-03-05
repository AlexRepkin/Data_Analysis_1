#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import secrets
import string
import sys


if __name__ == "__main__":
    # Создание пароля относительно переданной через командную строку его длины.
    if len(sys.argv) < 2:
        # Не передана длина пароля. Только имя файла.
        print("The password length is not given!", file=sys.stderr)
        sys.exit(1)
    chars = string.ascii_letters + string.punctuation + string.digits
    length_pwd = int(sys.argv[1])
    result = []
    for _ in range(length_pwd):
        # SystemRandom - класс, использующий функцию os.urandom() для генерации
        # случайных чисел из источников, предоставленных ОС.
        idx = secrets.SystemRandom().randrange(len(chars))
        result.append(chars[idx])
    print(f"Secret Password: {''.join(result)}")
