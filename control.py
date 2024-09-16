x = 0.0
y = 0.0
z = 0.0
yaw = 0.0
recording = False
frecord = True
recordcomplete = False
ConnectionOrder = False

def operate(code):
    global x, y, z, yaw, recording, frecord, ConnectionOrder
    frecord = recording
    x = code['dx']
    y = code['dy']
    z = code['dz']
    yaw = code['dyaw']
    recording = code['record']
    #print(f"{x} {y} {z} {yaw} {recording} {ConnectionOrder}")

