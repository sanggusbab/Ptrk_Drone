import subprocess
import time


while True:
    temp = subprocess.call(["vcgencmd", "measure_temp"])
    time.sleep(4)