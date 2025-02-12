import serial
import time
import tkinter as tk
from tkinter import ttk

# 아두이노와의 시리얼 포트 설정
port = 'COM5'  # 자신의 포트에 맞게 수정
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)  # 아두이노와 연결될 때까지 잠시 대기

# 서보 모터 제어 함수
def update_servo():
    servo_id = int(servo_var.get())  # 선택된 서보 ID
    angle = angle_slider.get()  # 슬라이더 값

    # 서보 ID와 각도를 아두이노로 전송 (예: "1,2048")
    ser.write(f"{servo_id},{int(angle)}\n".encode('utf-8'))

    # 현재 상태 표시
    angle_label.config(text=f"서보 {servo_id} 각도: {int(angle)}")

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("단일 서보 모터 제어")

# 서보 ID 선택 드롭다운
servo_var = tk.StringVar()
servo_var.set("0")  # 기본값: 서보 0

servo_label = ttk.Label(root, text="제어할 서보 선택")
servo_label.pack(pady=10)

servo_dropdown = ttk.Combobox(root, textvariable=servo_var, values=["0", "1", "2", "3", "4"])
servo_dropdown.pack()

# 서보 각도 조정 슬라이더
angle_label = ttk.Label(root, text="각도: 2048")
angle_label.pack(pady=10)

angle_slider = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
angle_slider.set(2048)  # 기본값 설정
angle_slider.pack()

# 값이 변경될 때마다 각도 레이블 업데이트
angle_slider.bind("<Motion>", lambda event: angle_label.config(text=f"각도: {int(angle_slider.get())}"))

# 업데이트 버튼
update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo)
update_button.pack(pady=20)

# Tkinter 이벤트 루프 시작
root.mainloop()

# 프로그램 종료 시 시리얼 포트 닫기
ser.close()
