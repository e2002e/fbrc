# fbrc
fbrc - FaceBook Recovery Cracker

Prerequisites:

- access to facebook
- target email or phone number
- pyton

Facebook recovery suffers from a security flaw, that is when user asks for a recovery code, it isn't required to enter this code in the formular for the new password's page to be created.
Thus it's possible to trigger the recovery process and then bruteforce the recovery url.

You can do this with any software or a simple program that will generate a million code (6 digits) and try a GET request like this:
You must pass the user_id as the script parameter, you will find this id in the souce code of the page on the wall of the user .
