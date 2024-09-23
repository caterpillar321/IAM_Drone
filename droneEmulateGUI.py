import tkinter as tk
from tkinter import ttk
import drone  # drone.py 모듈을 가져옴

labelRoll = None
labelPitch = None
labelYaw = None

def update_roll(value):
    # drone.py의 roll 값을 슬라이더 값으로 업데이트
    drone.roll = int(float(value))
    labelRoll.config(text=f"{drone.roll}")

def update_pitch(value):
    # drone.py의 roll 값을 슬라이더 값으로 업데이트
    drone.pitch = int(float(value))
    labelPitch.config(text=f"{drone.pitch}")

def update_yaw(value):
    # drone.py의 roll 값을 슬라이더 값으로 업데이트
    drone.yaw = int(float(value))
    labelYaw.config(text=f"{drone.yaw}")


def setGUI():
    global labelRoll, labelPitch, labelYaw
    # Tkinter 창 생성
    root = tk.Tk()
    root.title("Roll 슬라이더")
    root.geometry("300x400")

    # 레이블 생성
    labelRoll = tk.Label(root, text=f"{drone.roll}")
    labelRoll.pack(pady=10)

    # 슬라이더 생성
    sliderRoll = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_roll  # 슬라이더 값이 변경될 때 update_roll 함수 호출
    )
    sliderRoll.pack(pady=20)

    labelPitch = tk.Label(root, text=f"{drone.pitch}")
    labelPitch.pack(pady=10)

    sliderPitch = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_pitch  # 슬라이더 값이 변경될 때 update_roll 함수 호출
    )
    sliderPitch.pack(pady=20)

    labelYaw = tk.Label(root, text=f"{drone.yaw}")
    labelYaw.pack(pady=10)

    sliderYaw = ttk.Scale(
        root,
        from_=0,
        to=360,
        orient="horizontal",
        length=250,
        command=update_yaw  # 슬라이더 값이 변경될 때 update_roll 함수 호출
    )
    sliderYaw.pack(pady=20)

    # 메인 이벤트 루프 실행
    root.mainloop()



