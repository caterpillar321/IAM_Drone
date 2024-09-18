
import multiprocessing
import socket
import threading
import control
import drone
from sendStreamByCPU import sendV
from ipAutoFinder import BleTools
#from recorder import record
from utility import kill_process_on_port, get_local_ip, internetAvailable, check_existing_socket
import time
import json
import struct

def server():
    global isConnected
    try:
        with open('status.txt', 'w') as file:
            file.write('None')
            file.close()
        
        tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tsock.bind((Host, Port))

        tsockI = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsockI.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tsockI.bind((Host, PortInfo))
        
        print(f"Server listening on: {Host}")
        tsock.listen()
        tsockI.listen()
        
        sock, addr = tsock.accept()
        sockI, addr = tsockI.accept()
        
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sockI.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        print(f"Connected by {addr}")
        print(f"sock: {sock}")
        print(f"sockI: {sockI}")

        isConnected = True
        tsock.close()
        tsockI.close()

        manage_threads(sock, sockI, addr) 

    except OSError as e:
        print(f"error in connection: {e}")
        with open('status.txt', 'w') as file:
            file.write('Reconnection')
            file.close()

    
def recv(sock):
    global isConnected
    sock.settimeout(3)
    while isConnected:
        try:
            sizebuffer = sock.recv(4)
            size = struct.unpack('>I', sizebuffer)[0]
            buffer = sock.recv(size).decode()
            data = json.loads(buffer)
            control.operate(data)
            time.sleep(0.1)

        except (ConnectionAbortedError, ConnectionResetError, OSError, struct.error) as e:
            print(f"error in recv order: {e}")
            with open('status.txt', 'w') as file:
                file.write('Reconnection')
                file.close()
            isConnected = False
            break

def sendInfo(sockI):
    global pitch, yaw, roll
    print("Info send Connected")
    sockI.settimeout(3)
    try:
        while isConnected:
            roll = drone.roll
            pitch = drone.pitch
            yaw = drone.yaw
            if roll < 0:
                roll += 360
            if pitch < 0:
                pitch += 360
            if yaw < 0:
                yaw += 360

            message = json.dumps({
                "roll": f"{roll:03.0f}",
                "pitch": f"{pitch:03.0f}",
                "yaw": f"{yaw:03.0f}",
                "ralt": f"{(drone.relativeALT):03.0f}",
                "lat": f"{drone.lat}",
                "lng": f"{drone.lng}"
            })

            size = len(message.encode())
            if sockI.fileno() == -1:  
                break

            sockI.sendall(struct.pack(">L", size))
            sockI.sendall(message.encode())
            time.sleep(0.1)

    except (ConnectionAbortedError, ConnectionResetError, OSError) as e:
        print(f"error in sendinfo: {e}")
        with open('status.txt', 'w') as file:
            file.write('Reconnection')
            file.close()
        sockI.close()

def manage_threads(sock, sockI,  addr):
    global isConnected, cam, process
    if isConnected:
        tsockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsockL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tsockL.bind((Host, PortRV))
        tsockL.listen()
        sockL, addr = tsockL.accept()
        sockL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(f"sockL: {sockL}")
        tsockL.close()

        sizebuffer = sock.recv(4)
        size = struct.unpack('>I', sizebuffer)[0]
        buffer = sock.recv(size).decode()
        data = json.loads(buffer)
        width = data['width']
        height = data['height']
        fps = data['fps']
        cam = data['cam']

        with open('config.txt', 'w') as file:
            file.write(f"{width}\n")
            file.write(f"{height}\n")
            file.write(f"{fps}\n")
            file.close()

        thread2 = threading.Thread(target=recv, args=(sock, ))
        process2 = threading.Thread(target=sendInfo, args=(sockI,))
        threadcheck = threading.Thread(target=check_existing_socket, args=(sockI, ))
        
        thread2.start()
        process2.start() 
        threadcheck.start()
        print("threads start")

        if (cam == True):
            process = multiprocessing.Process(target=sendV, args=(Host, PortV))
            process.start()

        #threadRecord = multiprocessing.Process(target= record, args=(sockL, ))
        #threadRecord.start()
        
        while True:
            with open('status.txt', 'r') as file:
                try:
                    content = file.read()
                    if(content == 'Reconnection' and internetAvailable()):
                        print("Reconnecting...")
                        sock.close()
                        sockI.close()
                        sockL.close()
                        isConnected = False
                        time.sleep(3)
                        server_thread = threading.Thread(target=server)
                        server_thread.start()
                        with open('status.txt', 'w') as file:
                            file.write('None')
                            file.close()
                            if sock:
                                break
                except KeyboardInterrupt:
                    process.terminate()
                    isConnected = False
                    break
            time.sleep(5)
    
if __name__ == "__main__":
    with open('status.txt', 'w') as file:
        file.write('None')
        file.close()
    with open('record.txt', 'w') as file:
        file.write('None')
        file.close()

    cam = True
    local_ip = get_local_ip()
    Host = local_ip
    SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
    Port = 5000
    PortV = 5005
    PortInfo = 5010
    PortRV = 5015
    isConnected = False

    ble_tools = BleTools(SERVICE_UUID, CHARACTERISTIC_UUID)
    ble_tools.send_message_sync(Host)

    #drone.droneStart()
    server_thread = threading.Thread(target=server)
    server_thread.start()
