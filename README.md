# fbrc
fbrc - FaceBook Recovery Cracker

This software is not indented to be used by 'hackers' or 'crackers' to piss off people or take revenge, it is a proof of concept that unveils a flaw in the way facebook deals with password recovery in the hope that they fix it, if they don't then I'm not to be taken responsible for it, a child could have writen this code. Maybe they'll think about the end user and not about how much they earn.

Prerequisites: 
python2.7 and pip
access to facebook
target email

pip install socks
pip install numba

Usage:
Navigate to the target account and open the (infect) source code of the page, search for the value of USER_ID (something like 10003...)
Use tor browser and go to facebook's login page, select "Forgot Password ?" and enter the email, you'll be taken to the recovery option asking which method you want to use, choose email and make it send the code.

We are then ready to bruteforce, what are we attacking here ? Not the post form asking for the recovery code, because it locks after 20 attempts and reset. We are just bruteforcing the link created by facebook to change the password, link that has for sole definition a constant address followed by two values: the user ID that we retrieved and the recovery code... so 1 million try (6 digits) is the maximum we would have to do to get to the page. When done the software will give you that page.
