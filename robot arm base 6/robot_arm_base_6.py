import serial
import time
import tkinter as tk
from tkinter import ttk

port = 'COM5'
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)

def update_servo_angles():
    angle0 = slider0.get()
    angle1 = slider1.get()
    angle2 = slider2.get()
    angle3 = slider3.get()
    angle4 = slider4.get()
    angle5 = slider5.get()
    
    ser.write(f"{angle0},{angle1},{angle2},{angle3},{angle4},{angle5}\n".encode('utf-8'))

    angle0_label.config(text=f"각도 0: {int(angle0)}")
    angle1_label.config(text=f"각도 1: {int(angle1)}")
    angle2_label.config(text=f"각도 2: {int(angle2)}")
    angle3_label.config(text=f"각도 3: {int(angle3)}")
    angle4_label.config(text=f"각도 4: {int(angle4)}")
    angle5_label.config(text=f"각도 5: {int(angle5)}")

def stop_all_servos():
    slider0.set(2048)
    slider1.set(2048)
    slider2.set(2048)
    slider3.set(2048)
    slider4.set(2048)
    slider5.set(2048)

    ser.write("2048,2048,2048,2048,2048,2048\n".encode('utf-8'))

    angle0_label.config(text=f"각도 0: 2048")
    angle1_label.config(text=f"각도 1: 2048")
    angle2_label.config(text=f"각도 2: 2048")
    angle3_label.config(text=f"각도 3: 2048")
    angle4_label.config(text=f"각도 4: 2048")
    angle5_label.config(text=f"각도 5: 2048")

root = tk.Tk()
root.title("서보 모터 6개 각도 조정")

# 첫 번째 서보 (ID=0)
label0 = ttk.Label(root, text="서보 0 각도")
label0.pack(pady=5)
slider0 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider0.set(2048)
slider0.pack()
angle0_label = ttk.Label(root, text=f"각도 0: {int(slider0.get())}")
angle0_label.pack()

# 두 번째 서보 (ID=1)
label1 = ttk.Label(root, text="서보 1 각도")
label1.pack(pady=5)
slider1 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider1.set(2048)
slider1.pack()
angle1_label = ttk.Label(root, text=f"각도 1: {int(slider1.get())}")
angle1_label.pack()

# 세 번째 서보 (ID=2)
label2 = ttk.Label(root, text="서보 2 각도")
label2.pack(pady=5)
slider2 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider2.set(2048)
slider2.pack()
angle2_label = ttk.Label(root, text=f"각도 2: {int(slider2.get())}")
angle2_label.pack()

# 네 번째 서보 (ID=3)
label3 = ttk.Label(root, text="서보 3 각도")
label3.pack(pady=5)
slider3 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider3.set(2048)
slider3.pack()
angle3_label = ttk.Label(root, text=f"각도 3: {int(slider3.get())}")
angle3_label.pack()

# 다섯 번째 서보 (ID=4)
label4 = ttk.Label(root, text="서보 4 각도")
label4.pack(pady=5)
slider4 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider4.set(2048)
slider4.pack()
angle4_label = ttk.Label(root, text=f"각도 4: {int(slider4.get())}")
angle4_label.pack()

# 여섯 번째 서보 (ID=5)
label5 = ttk.Label(root, text="서보 5 각도")
label5.pack(pady=5)
slider5 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
slider5.set(2048)
slider5.pack()
angle5_label = ttk.Label(root, text=f"각도 5: {int(slider5.get())}")
angle5_label.pack()

slider0.bind("<Motion>", lambda event: angle0_label.config(text=f"각도 0: {int(slider0.get())}"))
slider1.bind("<Motion>", lambda event: angle1_label.config(text=f"각도 1: {int(slider1.get())}"))
slider2.bind("<Motion>", lambda event: angle2_label.config(text=f"각도 2: {int(slider2.get())}"))
slider3.bind("<Motion>", lambda event: angle3_label.config(text=f"각도 3: {int(slider3.get())}"))
slider4.bind("<Motion>", lambda event: angle4_label.config(text=f"각도 4: {int(slider4.get())}"))
slider5.bind("<Motion>", lambda event: angle5_label.config(text=f"각도 5: {int(slider5.get())}"))

update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo_angles)
update_button.pack(pady=20)

stop_button = ttk.Button(root, text="Stop (모두 2048로 설정)", command=stop_all_servos)
stop_button.pack(pady=20)

root.mainloop()

ser.close()
