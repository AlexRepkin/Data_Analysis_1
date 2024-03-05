#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re


# Полученный вариант - 9 (Номер по списку - 28).
if __name__ == "__main__":
    print("Good day! Which file would you like to open?")
    for _ in os.listdir():
        if os.path.isfile(_):
            print(f"File '{_}'")
    filename = input("Needed file: ")
    # Открытие файла в режиме чтения и запись данных из него в переменную.
    with open(filename, 'r') as file:
        # Создание списка из слов. [^a-z] - маска, говорящая не делить малые латинские буквы.
        # + означает, что эти буквы могут повторяться. Флаг заставляет игнорировать регистр букв.
        words = re.split('[^a-z]+', file.read(), flags=re.IGNORECASE)
    needed_words = []
    # Было сказано, что текст на английском.
    vowels = "aeiouAEIOU"
    for word in words:
        if len(word) > 0 and (word[0] in vowels) and (word[-1] in vowels):
            needed_words.append(word)
    if needed_words:
        print("Words, that start and end with vowels:", end=" ")
        for word in needed_words:
            print(word, end="; ")
    else:
        print("Text has no words, that start and end with vowels.")
