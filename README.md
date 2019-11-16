# fbrc
fbrc - FaceBook Recovery Cracker

Prerequisites:

python2.7 and pip

-access to facebook

-target email

pip install numba

Usage:

whith vpns (on on host, on in vm)
python fbrc.py
with tor
torsocks python fbrc.py

Navigate to the target account and open the source code of the page, search for the value of USER_ID (something like 10003...) copy it.
Use tor browser and go to facebook's login page, select "Forgot Password ?" and enter the email, you'll be taken to the recovery option asking which method you want to use, choose email and make it send the code.

We are then ready to bruteforce, what are we attacking here ? Not the post form asking for the recovery code, because it locks after 20 attempts and reset. We are just bruteforcing the link created by facebook to change the password, link that has for sole definition a constant address followed by two values: the user ID that we retrieved and the recovery code... so 1 million try (6 digits) is the maximum we would have to do to get to the page. When done the software will give you that page, you should be careful to open it via tor instead of rightcliking on it to open it via the terminal.
