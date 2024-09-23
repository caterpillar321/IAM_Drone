import threading
import control
import time

connection = None
droneID = None
droneComp = None

x = 0; y = 0; z = 0
roll = 10; pitch = 20; yaw = 30
lat = 37.5
lng = 127
relativeALT = 0
batteryRemain = 100
flightMode = "Stabilized"
lock = threading.Lock()

def getOp():
    global x, y, z, yaw
    while True:
        x = round(control.x * 10)
        y = round(control.y * 10)
        z = round(control.z * 10)
        yaw = round(control.yaw * 10)
        time.sleep(0.1)


