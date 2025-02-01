import serial
import time
import tkinter as tk
from tkinter import ttk

port = 'COM9'
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)

def update_servo_angle():
    angle = slider.get()

    ser.write(f"{int(angle)}\n".encode('utf-8'))

    angle_label.config(text=f"서보 각도: {int(angle)}")

def stop_servo():
    slider.set(2048)

    ser.write(f"2048\n".encode('utf-8'))

    angle_label.config(text="서보 각도: 2048")

root = tk.Tk()
root.title("서보 모터 제어")

label = ttk.Label(root, text="서보 각도 조절")
label.pack(pady=10)
slider = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider.set(2048)
slider.pack()

angle_label = ttk.Label(root, text=f"서보 각도: {int(slider.get())}")
angle_label.pack()

slider.bind("<Motion>", lambda event: angle_label.config(text=f"서보 각도: {int(slider.get())}"))

update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo_angle)
update_button.pack(pady=20)

stop_button = ttk.Button(root, text="Stop (2048로 설정)", command=stop_servo)
stop_button.pack(pady=20)

root.mainloop()

ser.close()
