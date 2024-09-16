from pymavlink import mavutil
import threading
import control
import time

connection = None
droneID = None
droneComp = None

x = 0; y = 0; z = 0
yaw = 0
roll = 10; pitch = 20; yaw = 30
lat = 37.5
lng = 127
relativeALT = 0
lock = threading.Lock()

def getOp():
    global x, y, z, yaw
    while True:
        x = round(control.x * 10)
        y = round(control.y * 10)
        z = round(control.z * 10)
        yaw = round(control.yaw * 10)
        droneMove(x, y, z, yaw)
        time.sleep(0.1)

def set():
    global connection, droneID, droneComp
    print("start to set")
    connection = mavutil.mavlink_connection('COM5', baud=57600)
    print("connect to FC")
    inform = connection.wait_heartbeat()
    print("get heartbeat")
    droneID = inform.get_srcSystem()
    droneComp = inform.get_srcComponent()
    connection.mav.command_long_send(
        droneID,
        droneComp,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0
    )
    print("connected to drone")
    connection.motors_armed_wait()
    print("drone set")
    threadGet = threading.Thread(target=getOp, daemon=True)
    threadGet.start()
    threadAttitude = threading.Thread(target=getAttitude)
    threadAttitude.start()

def droneMove(x, y, z, yaw):
    global droneComp, droneID
    if (x != 0) or (y != 0) or (z != 0) or (yaw != 0):
        print(f"order : {x} {y} {z} {yaw}")
    connection.mav.set_position_target_local_ned_send(
        0,             # time_boot_ms (not used)
        droneID,     
        droneComp,  
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # frame
        0b0000111111000111,  
        0, 0, 0,       
        x, y, z,    # x, y, z velocity in m/s
        0, 0, 0,     
        yaw, 0           # yaw, yaw_rate (not used)
    )

def getAttitude():
    global connection, roll, pitch, yaw, relativeALT
    while True:
        if connection is not None:
            msg = connection.recv_match(type='ATTITUDE')
            if msg is not None:
                with lock:
                    roll = msg.roll * 57.2958
                    pitch = msg.pitch * 57.2958
                    yaw = msg.yaw * 57.2958
                #print(f"Roll: {roll:.2f}, Pitch: {pitch:.2f}, Yaw: {yaw:.2f}")

def droneStart():
    set()

if __name__ == "__main__":
    droneStart()
