Fox-Latch
=========

Fox Latch is a web app built on Django (Python) that is used to 
remotely lock and unlock doors using a servo. It also checks the 
state of the door and lock using the servo position and a hall 
effect sensor. These are connected to a Raspberry Pi and broadcast 
behind the built in Django auth.

ALPHA BUILD COMPLETE: 1/2/2014
==============================

Working site, user registration, installer, and controller.

Current security holes:

  -A user can be created with the same IP as another, then
   access their lock.
   Resolution: Generate a SHA-2 256 bit key associated with
               the first instance of the IP, so that duplicate
               IP usage can only be achieved with the key.
               (this allows for roommates to have seperate
               accounts but still access the same door securley).

  -Not using ssl (https) so all passwords and such are submitted
   to the server via plaintext.
   Resolution: Add SSL cert capability, use Nginx or Apache to
               wrap web app with, unless Django has this ability.

Current bugs:

  -Submitting a login form with nothing in it returns an error.
   Resolution: Use built in Django auth/validation to return
               errors if fields are empty (just like with user
               registration).

  -When called, if completed successfully, the raspi assumes the
   servo turned even if servo is not connected. This doesn't pose
   too big of a problem, because when reconnected the servo may be
   in unlocked state even though it reads as locked. When next called
   it will not move but the status will change back to the correct
   status.
   Resolution: ???
   
  -Possible bug: May not ssh correctly on first time due to known
   hosts check.
   Resolution: Ignore known_hosts?
   
Things to impliment for beta:

  -SSL: jesus christ this needs to be up before it gets put on a door
  -Change IP form
  -Change password form
  -Permanent domain: foxlatch.csh.rit.edu
  -SHA-2 256 bit key generation for new IPs
  -Dissallow same ip for different account unless key used

Things to impliment for full release:

  -Dynamically check the status of the door for display on the page
   (could pose a problem seeing as what gets the status is the main
   program, which could cause some GPIO conflict, but I am unsure)
