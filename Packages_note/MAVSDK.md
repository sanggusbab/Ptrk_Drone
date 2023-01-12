# MAVSDK test
> pip3 install --user pyserial empty toml numpy pandas jinja2 pyyaml pyros-genmsg packaging

> wget https://github.com/mavlink/MAVSDK/releases/download/v0.37.0/mavsdk_0.37.0_ubuntu20.04_amd64.deb

> sudo dpkg -i mavsdk_0.37.0_ubuntu20.04_amd64.deb

> git clone https://github.com/mavlink/MAVSDK.git --recursive

test example

> cd ~/Downloads/MAVSDK/examples/takeoff_and_land/

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