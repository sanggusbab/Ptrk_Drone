# After RaspberryPi ssh Connect
cd Ptrk_Drone
git pull origin main

# Ptrk_Drone
Hands Drone Project

# settings on PC(Linux OS)
// Gazebo와 함께 PX4 AutoPilot실행
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
cd PX4-Autopilot/
bash ./Tools/setup/ubuntu.sh
./Tools/setup/ubuntu.sh --no-nuttx
./Tools/setup/ubuntu.sh --no-sim-tools
chmod +x ~/Downloads/gazebo.sh
gnome-terminal --working-directory="~" -e "./Downloads/gazebo.sh"

sudo apt-get install libboost-all-dev
sudo apt-get autoremove
sudo apt-get install libgazebo-dev
sudo apt install protobuf-compiler

cd PX4-Autopilot/
make px4_sitl gazebo
make px4_sitl list_vmd_make_targets

on Hompage Download Gazebo script

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