### Ptrk_Drone-Project
Hands Person Tracking Drone Project

# After RaspberryPi ssh Connect
htop
slurm -i enp0s3
python3 ~/Desktop/Ptrk_Drone/Rasp/Temp.py
cd ~/Desktop/Ptrk_Drone
git pull origin main

# settings on PC(Linux OS)
sudo apt install htop

cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

sudo apt-get install python3-pip -y
pip3 install --user future
sudo apt-get install python3-tk -y
sudo apt-get install git -y
sudo apt install vim
sudo apt-get install libjpeg-dev zlib1g-dev
cd ~/Downloads
git clone https://github.com/mavlink/mavlink.git --recursive
gedit ~/.bashrc
// export PYTHONPATH=/home/sanggu/Downloads/mavlink
echo $PYTHONPATH
python3 -m pymavlink.tools.mavgen --lang=Java --wire-protocol=2.0 --no-validate --output=/home/sanggu/Downloads/mavlink/out /home/sanggu/Downloads/mavlink/message_definitions/v1.0/test.xml
cd ~/Desktop
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
vim ~/Desktop/PX4-Autopilot/Tools/setup/requirements.txt
// sympy>=1.10.1 -->> sympy>=1.9
bash ~/Desktop/PX4-Autopilot/Tools/setup/ubuntu.sh
sudo apt update
sudo apt upgrade -y
~/Desktop/PX4-Autopilot/Tools/setup/ubuntu.sh --no-nuttx
~/Desktop/PX4-Autopilot/Tools/setup/ubuntu.sh --no-sim-tools
cd ~/Desktop/PX4-Autopilot/
make px4_sitl gazebo ********************************************************
// commander takeoff
// commander land
sudo usermod -a -G dialout $USER
sudo apt-get remove modemmanager -y
sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav -y
sudo apt install libqt5gui5 -y
sudo apt install libfuse2 -y
//download QGroundControl.AppImage
cd ~/Downloads
chmod +x ./QGroundControl.AppImage
~/Downloads/QGroundControl.AppImage ********************************************************
sudo apt-get update
sudo apt-get upgrade
sudo apt autoremove -y
sudo reboot

cd ~/PX4-Autopilot/
// gstreaming
gst-launch-1.0 -v udpsrc port=5600 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' \! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink fps-update-interval=1000 sync=false
gazebo --verbose
export VERBOSE_SIM=1
make px4_sitl gazebo

// param
param set NAV_RCL_ACT 0
param set NAV_DLL_ACT 0
param set SIM_BAT_MIN_PCT 10
param set SYS_FAILURE_EN 1
// on pxh
set SYS_FAILURE_EN 1
failure gps off
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
// ROS2
locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale
sudo apt update && sudo apt install curl gnupg2 lsb-release -y
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo sed -i -e 's/ubuntu .* main/ubuntu focal main/g' /etc/apt/sources.list.d/ros2.list
sudo apt update
sudo apt install ros-foxy-desktop
source /opt/ros/foxy/setup.bash
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
vi .bashrc
source /opt/ros/foxy/setup.bash
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
rqt graph
sudo apt update
sudo apt install ~nros-foxy-rqt*
rqt
sudo apt install ros-foxy-turtle-tf2-py ros-foxy-tf2-tools
pip3 install transforms3d
source /opt/ros/foxy/setup.bash
ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py
ros2 run turtlesim turtle_teleop_key
rviz2

# settings on raspi
pkg-config --modversion opencv4

sudo apt-get purge libopencv* python-opencv
sudo apt-get autoremove

// 기존 설치 제거!
sudo find /usr/local/ -name "*opencv*" -exec rm-i {} \;

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential cmake git unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgtk2.0-dev libcanberra-gtk*
sudo apt-get install python3-dev python3-numpy python3-pip
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev
sudo apt-get install libv4l-dev v4l-utils
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install libavresample-dev libvorbis-dev libxine2-dev
sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install liblapack-dev libeigen3-dev gfortran
sudo apt-get install libhdf5-dev protobuf-compiler
sudo apt-get install libprotobuf-dev libgoogle-glog-dev libgflags-dev
sudo apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
sudo sh -c "echo '/usr/local/cuda/lib64' >> /etc/ld.so.conf.d/nvdia-tegra.conf"
sudo ldconfig
sudo apt -y install gcc-8 g++-8
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8 --slave /usr/bin/g++ g++ /usr/bin/g++-8
sudo apt install libatlas-base-dev liblapacke-dev gfortran
sudo apt install libhdf5-dev libhdf5-103
sudo apt install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly

wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-64-bits/raw/main/OpenCV-4-5-5.sh
sudo chmod 755 ./OpenCV-4-5-5.sh
./OpenCV-4-5-5.sh

python3
import cv2
cv2.__version__
quit()