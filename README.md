# fbrc
fbrc - FaceBook Recovery Cracker


Prerequisites:

python3 !

-access to facebook

-target email

pip3 install -r requirements  
chmod +x fbrc.py  
./fbrc.py  

Usage:  

I suggest to simply (and safely) forward the program's connection through tor with a command like "tsocks python fbrc.py",  
If you have a vpn it will just be faster but less secured.  
1-On facebook, navigate to the target's wall and look at the source code of the page,  
search (ctrl+f) for the value of USER_ID (something like 10003...) and copy it.  

2-Go to facebook's login page, select "Forgot Password ?" and enter the email,  
you'll be taken to the recovery option asking which method you want to use.  
Choose email and make it send the code.  

3-Run fbrc.py and enter the user id, you'll be given the link to change the password in under 3 days if your network is not too slow.  

Notes:

Please don't victimize people.  
Make an effort and read the code.  

The password's changing page is an url defined by the user ID and the recovery code,  
Instead of bruteforcing the recovery code, we bruteforce the url of this page.  

Note that there might still be an impossibility to change the password because of IP addresses checks,  
I don't know if obtaining the recovery page url gives you a precedence over the registered IP, and I don't know about the timeout for this page.  

