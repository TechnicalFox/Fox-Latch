"""
Fox Latch: setup file

Objective: Have foxlatch easily setup with a single python file.

This implementation TechnicalFox.
"""
import os
import sys

""" Class that sets up a raspi for foxlatch. """
class foxlatch_setup(object):

    """ Called when object created, makes install dir and sets public key variable. """
    def __init__(self):
        os.system("mkdir ~/.foxlatch")
        #public key to allow ssh commands from server
        self.public_key = "\nssh-dss AAAAB3NzaC1kc3MAAACBAJxbrfvPFYbuDQjltl6djhZIgVNhnuA4KhG13cXF/xzb+4QX9lKWaG1pf9FtRP1mJs72qyo1PcXSV32yllW/Z/mL0OOaj3SdbIPEExczxaZZsIte11v48fBPLPYFLamF3GPYNoKkJrKgAfdqu+onjIk4ToDpmDgYud+thTnYBTKBAAAAFQDnj2Hy5GXm9dnBekxy/dItjbKuAQAAAIBecw1pYT2Copui3dZ7HLGkkyOo147WTIuz5EukquniuMiX4NKYYJdhw0imu+shY618YO7/lb8X4yl/gU74eouKWpK0bPgRdaiyC6b9eSMi9mLVBXCddj9GGMSu3xK1bf4LvFKoyrXhmpHiaOxlLDGxFCbYoeMkj5L4P7M6Vs76tAAAAIAEcIR1VEf00sliO6sibTznCVf/hNy84Gv2GrnlgC2HYGwwHmX+yVz0C2n80ISZPH7shAk320lU42ccyM9rW9SKJ9YXHtOHP3Mw+8dNUYqcgSqDEyhxUosNX++v67ZwD8hQJEeywfA1cUeN9pawAnKf2iA9B0WRJAitQFwAijhuxg== technicalfox@san.csh.rit.edu"
    
    """ Function that installs ssh, configures it, and makes it start on boot. """
    def setup_ssh(self):
        os.system("sudo apt-get install ssh")
        os.system("sudo update-rc.d ssh defaults")
        os.system("wget ~/.foxlatch csh.rit.edu:3333/sshd_config")
        os.system("sudo mv ~/.foxlatch/sshd_config /etc/ssh/")

    """ Function that adds the public key to the authorized_keys file. """
    def add_key(self):
        authorized_keys = open("/home/pi/.ssh/authorized_keys", "a+")
        key_present = False
        for line in authorized_keys:
            if line == self.public_key: key_present = True
        if key_present = False: authorized_keys.write(self.public_key)
        authorized_keys.close()

    """ Function that retrieves the foxlatch code. """
    def get_foxlatch(self):
        os.system("wget -P ~/.foxlatch csh.rit.edu:3333/foxlatch.py")

################################
### END foxlatch_setup class ###
################################

"""
Main function, checks if run as root, if not it quits.
Asks user if sure about running, then sets up foxlatch
using the foxlatch_setup class.
"""
if __name__ == "__main__":
    if not os.geteuid() == 0: sys.exit('foxlatch_setup.py must be run as root')
    prompt = None
    while prompt != 'y' and prompt != 'n' and prompt != 'Y' and prompt != 'N':
        if prompt != None: prompt = raw_input("Please type upper or lower case 'y' or 'n' only.")
        else: prompt = raw_input("This program installs ssh, changes ssh settings, and downloads files. Are you sure you want to do this? y/n")
    if prompt == 'y' or prompt == 'Y':
        foxlatch = foxlatch_setup()
        print("Setting up ssh...")
        foxlatch.setup_ssh()
        print("Adding public key...")
        foxlatch.add_key()
        print("Downloading foxlatch...")
        foxlatch.get_foxlatch()
        print("Setup complete.")
    else: print("Setup aborted.")
    sys.exit()
