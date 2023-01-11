****************** The Basic Env ******************
sudo apt-get install python3-pip
pip3 install --user future
sudo apt-get install python-tk
cd ~/Downloads
git clone https://github.com/mavlink/mavlink.git
git submodule update --init --recursive
PYTHONPATH=/home/pi/Downloads/mavlink
export PYTHONPATH
python -m mavgenerate

locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale

sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install -y \
  libbullet-dev \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools
    # install some pip packages needed for testing
python3 -m pip install -U \
  argcomplete \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest
    # install Fast-RTPS dependencies
sudo apt install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev
    # install Cyclone DDS dependencies
sudo apt install --no-install-recommends -y \
  libcunit1-dev
mkdir -p ~/ros2_foxy/src
cd ~/ros2_foxy
vcs import --input https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos src
sudo apt update
sudo apt upgrade
cd ~/ros2_foxy/
colcon build --symlink-install
    # Replace ".bash" with your shell if you're not using bash
    # Possible values are: setup.bash, setup.sh, setup.zsh
. ~/ros2_foxy/install/local_setup.bash
. ~/ros2_foxy/install/local_setup.bash
ros2 run demo_nodes_cpp talker
. ~/ros2_foxy/install/local_setup.bash
ros2 run demo_nodes_py listener
sudo apt install clang
export CC=clang
export CXX=clang++
colcon build --cmake-force-configure
rm -rf ~/ros2_foxy
sudo apt update
sudo apt upgrade
sudo apt-get autoremove
sudo apt install ros-foxy-rmw-fastrtps-cpp
cd ros2_ws/src
git clone https://github.com/ros2/rmw_fastrtps ros2/rmw_fastrtps
git clone https://github.com/eProsima/Fast-DDS eProsima/fastrtps
cd ..
rosdep install --from src -i
colcon build --symlink-install
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_cpp listener






****************** On Laptop *********************
locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale