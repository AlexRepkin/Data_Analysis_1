#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import string
import shutil
import secrets


def generating(name):
    with open(name, "w") as file:
        chars = string.ascii_letters + string.punctuation + string.digits
        result = []
        for _ in range(5):
            result.append(chars[secrets.SystemRandom().randrange(len(chars))])
        file.write("".join(result))


if __name__ == "__main__":
    os.mkdir("Temporary")
    os.chdir("Temporary")
    amount = int(
        input("Good day! How many variants are needed to be combined? Amount = "))
    for i in range(amount):
        generating(str(i) + ".txt")
    password = ""
    for i in range(amount):
        with open(f"{i}.txt", "r") as file:
            password += file.read()
    os.chdir("../")
    with open("final.txt", "w") as final_file:
        final_file.write(password)
    answer = input("Would you like to delete temporary files? (Y/N) - ")
    if (answer == "Y"):
        shutil.rmtree("Temporary")
