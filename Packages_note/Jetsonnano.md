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

> make px4_sitl gazebo

# QGroundControl
> sudo usermod -a -G dialout $USER

> sudo apt-get remove modemmanager -y

> sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y

> sudo apt install libqt5gui5 -y

> sudo apt install libfuse2 -y

> chmod +x ~/Downloads/QGroundControl.AppImage

> ~/Downloads/QGroundControl.AppImage

>

# MAVSDK test

> wget https://github.com/mavlink/MAVSDK/releases/download/v0.37.0/mavsdk_0.37.0_ubuntu20.04_amd64.deb

> sudo dpkg -i mavsdk_0.37.0_ubuntu20.04_amd64.deb

> git clone https://github.com/mavlink/MAVSDK.git --recursive

> cd MAVSDK

> cd examples

> cd takeoff_and_land/

> cmake -Bbuild -H.

> cmake --build build -j4

> build/takeoff_and_land udp://:14540

> cd ~/Downloads/PX4-Autopilot

> DONT_RUN=1 make px4_sitl gazebo mavsdk_tests

> test/mavsdk_tests/mavsdk_test_runner.py test/mavsdk_tests/configs/sitl.json --speed-factor 10

> test/mavsdk_tests/mavsdk_test_runner.py test/mavsdk_tests/configs/sitl.json --speed-factor 10 --model tailsitter --case 'Fly square Multicopter Missions including RTL'

# MAVSDK python

> pip3 install mavsdk

> pip3 install aioconsole

    from mavsdk import System
    drone = System()
    await drone.connect()
    await drone.action.arm()
    await drone.action.takeoff()
    raise ActionError(result, “arm()”)
    await drone.action.land()