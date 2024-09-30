import tkinter as tk
from tkinter import ttk
import drone  

labelRoll = None
labelPitch = None
labelYaw = None
labelAlt = None
labelBattery = None
labelLat = None
labelLng = None

def update_roll(value):
    drone.roll = int(float(value))
    labelRoll.config(text=f"{drone.roll}")

def update_pitch(value):
    drone.pitch = int(float(value))
    labelPitch.config(text=f"{drone.pitch}")

def update_yaw(value):
    drone.yaw = int(float(value))
    labelYaw.config(text=f"{drone.yaw}")

def update_alt(value):
    drone.relativeALT = int(float(value))
    labelAlt.config(text=f"{drone.relativeALT}")

def update_battery(value):
    drone.batteryRemain = int(float(value))
    labelBattery.config(text=f"{drone.batteryRemain}")

def update_lat():
    currentlat = entrylat.get()
    drone.lat = currentlat
    labelLat.config(text=f"{drone.lat}")

def update_lng():
    currentlng = entrylng.get()
    drone.lng = currentlng
    labelLng.config(text=f"{drone.lng}")


def update_mode(value):
    drone.flightMode = value


def setGUI():
    global labelRoll, labelPitch, labelYaw, labelAlt, labelBattery, labelLat, labelLng, entrylat, entrylng
    root = tk.Tk()
    root.title("DRONE GUI")
    root.geometry("300x1000")


    labelRollText = tk.Label(root, text="roll")
    labelRollText.pack(pady=1)
    labelRoll = tk.Label(root, text=f"{drone.roll}")
    labelRoll.pack(pady=1)
  
    sliderRoll = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_roll  
    )
    sliderRoll.pack(pady=2)


    labelPitchText = tk.Label(root, text="pitch")
    labelPitchText.pack(pady=1)
    labelPitch = tk.Label(root, text=f"{drone.pitch}")
    labelPitch.pack(pady=1)
    
    sliderPitch = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_pitch  
    )
    sliderPitch.pack(pady=2)


    labelYawText = tk.Label(root, text="yaw")
    labelYawText.pack(pady=1)
    labelYaw = tk.Label(root, text=f"{drone.yaw}")
    labelYaw.pack(pady=1)
    
    sliderYaw = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_yaw  
    )
    sliderYaw.pack(pady=2)


    labelAltText = tk.Label(root, text="Altitude")
    labelAltText.pack(pady=1)
    labelAlt = tk.Label(root, text=f"{drone.relativeALT}")
    labelAlt.pack(pady=1)
    
    sliderYaw = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_alt  
    )
    sliderYaw.pack(pady=2)


    labelBatteryText = tk.Label(root, text="Battery")
    labelBatteryText.pack(pady=1)
    labelBattery = tk.Label(root, text=f"{drone.batteryRemain}")
    labelBattery.pack(pady=1)
    
    sliderYaw = ttk.Scale(
        root,
        from_=0,
        to=100,
        orient="horizontal",
        length=250,
        command=update_battery
    )
    sliderYaw.pack(pady=2)

    entrylat = ttk.Entry(root)
    entrylat.pack(pady=1)
    labelLatText = ttk.Label(root, text="latitude")
    labelLatText.pack(pady=1)
    labelLat = ttk.Label(root, text=f"{drone.lat}")
    labelLat.pack(pady=1)

    buttonlat = tk.Button(root, text="set lat", command=update_lat)
    buttonlat.pack(pady=1)

    entrylng = ttk.Entry(root)
    entrylng.pack(pady=1)
    labelLngText = ttk.Label(root, text="longtitude")
    labelLngText.pack(pady=1)
    labelLng = ttk.Label(root, text=f"{drone.lng}")
    labelLng.pack(pady=1)

    buttonlng = tk.Button(root, text="set lng", command=update_lng)
    buttonlng.pack(pady=1)



    labelModeText = tk.Label(root, text="FlightMode")
    labelModeText.pack(pady=1)

    options = ["Stabilized", "Offboard", "Manual"]
    # 기본 선택값을 저장하는 변수
    selected_option = tk.StringVar()
    selected_option.set(options[0])
    option_menu = tk.OptionMenu(root, selected_option, *options, command=update_mode)
    option_menu.pack(pady=2)

    root.mainloop()
