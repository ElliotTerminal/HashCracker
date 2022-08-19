# -*- coding: UTF-8 -*-
# ToolName   : HashCracker
# Author     : ElliotTerminal
# License    : GPL V3
# Copyright  : ElliotTerminal (2022-2023)
# Github     : https://github.com/ElliotTerminal
# Description: HashCracker is a hash cracking tool in python
# Language   : Python
# If you copy open source code, consider giving credit



import hashlib

print(r"              ______ .______          ___       ______  __  ___  _______ .______                    ")
print(r"             /      ||   _  \        /   \     /      ||  |/  / |   ____||   _  \                   ")
print(r"            |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |                  ")
print(r"            |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /                   ")
print(r"            |  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \____              ")
print(r"             \______||__| `._____/__/     \__\ \______||__|\__\ |_______||__| \______|              ")
print(r"                                                                     - by ElliotTerminal")
print()

flag = 0
counter = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    
    enc_wrd = word.encode("utf-8")
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()


    # print(word)
    # print(digest)
    # print(pass_hash)
    counter += 1

    if digest == pass_hash:
        print("Password found")
        print("Password is " + word)
        flag = 1
        break

if flag == 0:
    print("Password/Passphrase is not in the list")
    
