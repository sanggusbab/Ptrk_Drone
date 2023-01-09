### Ptrk_Drone-Project
Hands Person Tracking Drone Project

# After ssh Connect
cd ~/Desktop/Ptrk_Drone
git pull origin main
python3 ~/Desktop/Ptrk_Drone/Rasp/Temp.py
htop
slurm -i enp0s3

# Other ways to install OpenCV
wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-64-bits/raw/main/OpenCV-4-5-5.sh
sudo chmod 755 ./OpenCV-4-5-5.sh
./OpenCV-4-5-5.sh

# On Raspberry Pi
1. Ubuntu 20.04
2. ROS2 / Mavros
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