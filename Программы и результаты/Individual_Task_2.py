#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re


# Полученный вариант - 13 (Номер по списку - 28).
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments! File's name is missing!")
        sys.exit(1)
    text = []
    try:
        # Открытие файла в режиме чтения и запись данных из него в переменную.
        with open(sys.argv[1], 'r') as file:
            for line in file:
                # Создание списка из строк. [^a-z] - маска, говорящая не делить малые латинские буквы.
                # + означает, что эти буквы могут повторяться. Флаг заставляет игнорировать регистр букв.
                text.append(re.split('[^a-z]+', line, flags=re.IGNORECASE))
        last_word = ""
        line_num = 0
        for line in text:
            line_num += 1
            if (len(line) > 2):
                for word in line:
                    if last_word == word:
                        print(
                            f"In line number {line_num}, word {word} is spelled twice.")
                    last_word = word
    except FileNotFoundError:
        print(f"Error! File not found.")
        sys.exit(1)
