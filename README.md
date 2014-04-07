Fox-Latch
=========

######Fox Latch is a web app built on Django (Python) that is used to remotely lock and unlock doors using a servo. It also checks the state of the door and lock using the servo position and a hall effect sensor. These are connected to a Raspberry Pi and broadcast behind the built in Django auth.

ALPHA BUILD COMPLETE: 4/2/2014
------------------------------

######Working site (user registration, login, and profile), installer, and controller.
######Strikethroughs are completed tasks.


###Current security holes:

  -~~A user can be created with the same IP as another, then access their lock. Resolution: Generate a SHA-2 256 bit key associated with the first instance of the IP, so that duplicate IP usage can only be achieved with the key. (this allows for roommates to have seperate accounts but still access the same door securley).~~

  -Not using ssl (https) so all passwords and such are submitted to the server via plaintext. Resolution: Add SSL cert capability. Will be using Apache and mod_wsgi.


###Current bugs:

  -~~Submitting a login form with nothing in it returns an error. Resolution: Use built in Django auth/validation to return errors if fields are empty (just like with user registration).~~

  -When called, if completed successfully, the raspi assumes the servo turned even if servo is not connected. This doesn't pose too big of a problem, because when reconnected the servo may be in unlocked state even though it reads as locked. When next called it will not move but the status will change back to the correct status. Resolution: ???
   
  -When called on a new ip, it hangs on whether or not to add it to known hosts indefinately. If it is a wrong address, but still a system configured for ssh, then it will hang on the password prompt (if manually passed by known hosts prompt) indefinately. Resolution: Use a python module to handle ssh instead of subprocess, possibly paramiko.
  
  -When setup file is run more than once it writes copies of files to the .foxlatch directory with different names (possibly also in /etc/ssh), and appends the publickey to the authorized\_keys file reguardless of whether or not it's there. Resolution: Fix the check to make sure publickey is not already contained in the authorized\_keys file, and have it overwrite old files in the .foxlatch directory.

   
###Things to impliment for beta:

  -Permanent domain (foxlatch.csh.rit.edu) & SSL: technically one task, can be done using Apache and mod_wsgi

  -~~Change IP form~~

  -Change password form

  -SHA-2 256 bit key generation for new IPs

  -~~Dissallow same ip for different account~~ unless key used


###Things to impliment for full release:

  -Dynamically check the status of the door for display on the page (could pose a problem seeing as what gets the status is the main program, which could cause some GPIO conflict, but I am unsure)
   
  -Use CSH Webauth for authentication instead of Django auth (this combined with ssl for the actual site will add more security, should be able to wrap some sort of output from webauth in an object with the IPv4 field instead of the current implimentation that wraps a Django auth user object and an IPv4 field in an object)

  -IPv6 (if you can even call ssh on IPv6 addresses)
  
  -Hostnames (could pose security threat if not sanitized correctly: injection to subprocess.call/subprocess.Popen in Python)
