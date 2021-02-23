# wctc-iot

##Pi Setup
1. Connect pi to usb / serial cable and connect usb end to pc
2. Power up pi
3. Open Putty - select serial connection, enter COM4 (Use device mgr to ensure correct com port) as serial line, enter 
4. Select serial connection
5. Enter COM4 as serial line (use device mgr to ensure correct com port)
6. Enter 115200 for speed
7. Click Open 
8. Press enter
9. Login to pi: username: pi, password: raspberry
10. Type the following commands: cd Desktop, bash network.sh (enter network user id / password)
11. After reboot, establish putty session and type the following command: hostname -I
12. Open VNC Viewer 
13. Enter ip address from step 6
14. Enter pi login credentials (pi, raspberry)
