#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Открытие файла в режиме записи. Если файл не найден - создаётся с именем text.txt.
    # encoding указывает используемую в файле кодировку.
    with open("text.txt", "w", encoding="utf-8") as fileptr:
        # Запись данных в файл.
        print("UTF-8 is a variable-width character encoding used for electronic communication.", file=fileptr)
        print("UTF-8 is capable of encoding all 1,112,064 valid character codepoints.", file=fileptr)
        print("In Unicode using one to four one-byte (8-bit) code units.", file=fileptr)
