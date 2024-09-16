
import os
import signal
import subprocess
import netifaces
import socket
import time
import select

def kill_process_on_port(port):
    # Find the process ID (PID) using lsof
    try:
        result = subprocess.check_output(["lsof", "-t", f"-i:{port}"])
        pids = result.decode().strip().split("\n")
        
        for pid in pids:
            try:
                os.kill(int(pid), signal.SIGKILL)
                print(f"Process {pid} on port {port} has been terminated.")
            except OSError as e:
                print(f"Error terminating process {pid}: {e}")
    except subprocess.CalledProcessError as e:
        print(f"No process found on port {port}")

def get_local_ip():
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for address in addresses[netifaces.AF_INET]:
                ip = address['addr']
                if ip != '127.0.0.1':
                    return ip
    return None

def internetAvailable():
    try:
        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockt.settimeout(3)
        sockt.connect(('8.8.8.8', 53))
        return True
    except socket.error:
        return False

def check_existing_socket(sock, interval=5):
    while True:
        try:
            # 소켓에 읽기, 쓰기, 예외 상태 확인
            readable, writable, exceptional = select.select([sock], [sock], [sock], 5)
            if readable:
                data = sock.recv(1024)
                if not data:
                    print("Socket connection closed by the remote host")
                    break
                print("Received data from socket:", data)
            if writable:
                print("Socket is writable")
            if exceptional:
                print("Socket has an exceptional condition")
                break

        except socket.error as e:
            print(f"Socket error: {e}")
            with open('status.txt', 'w') as file:
                file.write('Reconnection')
                file.close()
            break
        except ValueError as e:
            print(e)
            break

        time.sleep(interval)
