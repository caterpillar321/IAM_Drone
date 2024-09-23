import tkinter as tk
from tkinter import ttk
import drone  

labelRoll = None
labelPitch = None
labelYaw = None

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
    labelYaw.config(text=f"{drone.relativeALT}")


def setGUI():
    global labelRoll, labelPitch, labelYaw, labelAlt
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

    root.mainloop()
