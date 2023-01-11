# Ptrk_Drone-Project
Hands Person Tracking Drone Project
Korea University

# After ssh Connect
1. cd ~/Desktop/Ptrk_Drone
2. git pull origin main
3. python3 ~/Desktop/Ptrk_Drone/Rasp/Temp.py
4. htop
5. slurm -i enp0s3

# On RaspberryPi or JetsonNano
1. Linux OS
2. ( ROS | ROS2 ) & Mavros
3. Gazebo
6. MavRos Test
7. modudculab_ros package test
8. 01 Pixhawk & Raspberry Pi Connection
8. 04 Pixhawk flight mode select (position hold | mission mode | offboard)

# On Pixhawk
4. USB to TTL Connection : Laptop
8. 02 Raspberry Pi Power (Or Separated Battery)
9. Trajectory node

# Laptop (Windows 10)
5. QgroundControl 설치
8. 03 Raspberry Pi와 ssh 연결 (핫스팟)
10. Flight mode & Auto Mode (MissionPlanner | QgroundControl)

# Recommended Development Environment
- Ubuntu 20.04
- python3.8
- opencv 4.5

# Other ways to install OpenCV
1. wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-64-bits/raw/main/OpenCV-4-5-5.sh
2. sudo chmod 755 ./OpenCV-4-5-5.sh
3. ./OpenCV-4-5-5.sh

## package info exploring (python)
>>> import inspect

>>> inspect.getfile(/packagename)

>>> print(dir(/packagename))