# ToolChain & gazebo
> cd ~/Downloads

> git clone https://github.com/PX4/PX4-Autopilot.git --recursive

> bash ~/Downloads/PX4-Autopilot/Tools/setup/ubuntu.sh

reboot computer

> arm-none-eabi-gcc --version

> sudo apt-get install -y gcc-8-arm-linux-gnueabihf g++-8-arm-linux-gnueabihf

> sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-8 100 --slave /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-8

> sudo update-alternatives --config arm-linux-gnueabihf-gcc

> cd ~/Downloads/PX4-Autopilot

> sudo apt-get install -y gcc-8-aarch64-linux-gnu g++-8-aarch64-linux-gnu

> sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcc aarch64-linux-gnu-gcc /usr/bin/aarch64-linux-gnu-gcc-8 100 --slave /usr/bin/aarch64-linux-gnu-g++ aarch64-linux-gnu-g++ /usr/bin/aarch64-linux-gnu-g++-8

> sudo update-alternatives --config aarch64-linux-gnu-gcc
 
or

> sudo apt-get install -y gcc-8-aarch64-linux-gnu g++-8-aarch64-linux-gnu

> sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcc aarch64-linux-gnu-gcc /usr/bin/aarch64-linux-gnu-gcc-8 100 --slave /usr/bin/aarch64-linux-gnu-g++ aarch64-linux-gnu-g++ /usr/bin/aarch64-linux-gnu-g++-8

> sudo update-alternatives --config aarch64-linux-gnu-gcc

then

> cd ~/Downloads/PX4-Autopilot

> make px4_sitl gazebo