# fbrc
fbrc - FaceBook Recovery Cracker

Prerequisites:

python2.7 and pip

-access to facebook

-target email

pip install numba urllib httlib

Usage:
This will work BUT it's RISKY ! 
You don't want to give your ip to zuckeberg while you'r cracking facebook !!!
I suggest for noobs to simply forward the program's connection trhough tor with a command like "tsocks python fbrc.py"

For max speed, take some time to configure things well:
If you know a little what you are doing you can use vpn, but a vpn is never safe as it can be disconnected (because they fight back or some other reasons)
When doing this you must set up a virtual machine (virtualbox), and have a vpn running in both the host and the vm.
These vpns must not be configured with network-manager, they must be a system service, to be able to restart on failure.
Don't use the ubuntu version above 16 for that purpose because command line vpn is broken, and leaks dns, which leads to your ip, only use the version with resolvconf and not 
systemd-resolved.

example service settings as /etc/systemd/system/vpn.service 
don't use the name openvpn it's taken already.

-----------
[Service]
ExecStart=/usr/sbin/openvpn /pathtoyourvpnconfigfile
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
-----------
The Install section parameter is only to be able to do a service enabling in the vm (don't mistake enable with start)
Once you have this file created you are able to do a systemctl start vpn, check it worked with systemctl status vpn, and check you'r safe on dnsleaktest.com
There is no way your host vpn will get disconnected in the 20-30 seconds the vm one will take to reconnect overall. This is a pro tip you should cherish.

Navigate to the target account and open the source code of the page, search for the value of USER_ID (something like 10003...) copy it.
Use tor browser and go to facebook's login page, select "Forgot Password ?" and enter the email, you'll be taken to the recovery option asking which method you want to use,
choose email and make it send the code.

We are then ready to bruteforce, skip reading this if you are not interested in technical explaniations.
What are we attacking here ? Not the post form asking for the recovery code, because it locks after 20 attempts and reset.
We are just bruteforcing the link created by facebook to change the password, link that has for sole definition a constant address followed by two values:
the user ID that we retrieved and the recovery code... so 1 million try (6 digits) is the maximum we would have to do to get to the page.
When done the software will give you that page, you should be careful to open it via tor instead of rightcliking on it to open it via the terminal.
