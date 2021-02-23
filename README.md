# wctc-iot

## Pi Setup
1. Connect pi to usb / serial cable and connect usb end to pc
2. Power up pi
3. Open Putty - select serial connection, enter COM4 (Use device mgr to ensure correct com port) as serial line, enter 
     a. Select serial connection
     b. Enter COM4 as serial line (use device mgr to ensure correct com port)
     c. Enter 115200 for speed
     d. Click Open 
     e. Press enter
4. Login to pi: username: pi, password: raspberry
5. Type the following commands: cd Desktop, bash network.sh (enter network user id / password)
6. After reboot, establish putty session and type the following command: hostname -I
7. Open VNC Viewer 
     a. Enter ip address from step 6
     b. Enter pi login credentials (pi, raspberry)
