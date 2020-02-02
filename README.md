# fbrc
fbrc - FaceBook Recovery Cracker


Prerequisites:

python2.7 and pip2

-access to facebook

-target email

pip2 install numba urllib httlib


Usage:

I suggest to simply (and safely) forward the program's connection through tor with a command like "tsocks python fbrc.py"

1-On facebook, navigate to the target 'wall' and look at the source code of the page, search (ctrl+f) for the value of USER_ID (something like 10003...) copy it.

2-Use tor browser and go to facebook's login page, select "Forgot Password ?" and enter the email, you'll be taken to the recovery option asking which method you want to use.
Choose email and make it send the code. (it's also possible to do it with the phone number but requires a tweak of the code and i'll only do it upon request via issues)

3-Run fbrc.py and enter the user id, you'll be given the link to change the password in under 3 days if your network is not too slow.

!!!the link will be output in the terminal so DON'T BE A DICK and try to right click on it to open it, instead, use tor browser and paste the link in the address bar!!!

Notes:

Please don't victimize people.

Make an effort and read the code (it could be a virus right ?).

Nothing really magical but for the foolishness of facebook's design that allows that: the recovery page is a static url that has the user id and the recovery code as a parameter, that is all and you might understand now how it's easily hacked.
The password's changing page might expires but you'll usually get the link before it does, so if it fails repeat the whole procedure (from step 2) before filling and issue.


