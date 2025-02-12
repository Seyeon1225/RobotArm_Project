import serial
import time
import tkinter as tk
from tkinter import ttk

port = 'COM5'
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)

def update_servo():
    servo_id = int(servo_var.get())
    angle = angle_slider.get() 

    ser.write(f"{servo_id},{int(angle)}\n".encode('utf-8'))


    angle_label.config(text=f"서보 {servo_id} 각도: {int(angle)}")


root = tk.Tk()
root.title("단일 서보 모터 제어")


servo_var = tk.StringVar()
servo_var.set("0") 

servo_label = ttk.Label(root, text="제어할 서보 선택")
servo_label.pack(pady=10)

servo_dropdown = ttk.Combobox(root, textvariable=servo_var, values=["0", "1", "2", "3", "4"])
servo_dropdown.pack()


angle_label = ttk.Label(root, text="각도: 2048")
angle_label.pack(pady=10)

angle_slider = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
angle_slider.set(2048)
angle_slider.pack()

angle_slider.bind("<Motion>", lambda event: angle_label.config(text=f"각도: {int(angle_slider.get())}"))

update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo)
update_button.pack(pady=20)

root.mainloop()

ser.close()
