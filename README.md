# Ansible-playbook-for-GCI-2018

To get the playbook up and running with no error then follow these steps:

1. Get your hands on a raspberry pi, a DHT11 sensor and a breadboard with some jumper cables.

2.  Install raspbian on the raspberry pi and enable SSH.

3.  Install Fedora or Red hat linux in a virtual machine.

4. Install ansible on Fedora/Red hat linux

5. Add a root password to your raspberry pi because it does not have a root password by default but SSH requires it and you will easily
get root access to everything.

6. SSH in the raspberry pi to see if everything is working.

7. Then you will need to save the SSH public key and private key through this command:

   ssh-copy-id root@(raspberry pi ip address)
   
8. Then run the playbook with this command:

  ansible-playbook (name of the file).yml
  

If all goes well then good for you but if your encountering some errors then please let me know and I will try provide a fix.
