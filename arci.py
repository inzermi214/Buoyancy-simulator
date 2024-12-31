import tkinter as tk
from tkinter import messagebox, Canvas

# 메인 윈도우 초기화
root = tk.Tk()
root.title("부력 계산기")
root.geometry("600x600")

# 유체 밀도 입력 필드 생성
label_density = tk.Label(root, text="유체의 밀도 (kg/m³):")
label_density.pack()
entry_density = tk.Entry(root)
entry_density.pack()

# 잠긴 부피 입력 필드 생성
label_volume = tk.Label(root, text="잠긴 부피 (m³):")
label_volume.pack()
entry_volume = tk.Entry(root)
entry_volume.pack()

def calculate_buoyancy(density, volume):
    """
    부력 계산 함수
    density: 유체의 밀도 (kg/m³)
    volume: 잠긴 부피 (m³)
    """
    g = 9.8  # 중력 가속도 (m/s²)
    buoyancy_force = density * volume * g
    return buoyancy_force

def draw_sphere(canvas, water_level, sphere_top, sphere_bottom):
    """
    구를 그리는 함수
    canvas: 그리기 위한 캔버스
    water_level: 수면 높이
    sphere_top: 구의 윗부분 y좌표
    sphere_bottom: 구의 아랫부분 y좌표
    """
    canvas.create_line(0, water_level, 400, water_level, fill='blue')  # 수면 표시
    canvas.create_oval(190, sphere_top, 210, sphere_bottom, fill='orange')  # 구 그리기

def on_calculate():
    """
    계산 및 시각화 처리 함수
    """
    try:
        density = float(entry_density.get())  # 유체 밀도
        volume = float(entry_volume.get())   # 입력된 잠긴 부피
        buoyancy_force = calculate_buoyancy(density, volume)

        # 캔버스 초기화
        canvas.delete("all")

        # 수면 높이 설정
        water_level = 300

        # 구의 부피 및 지름 설정
        sphere_diameter = 40  # 구의 지름 (m)
        sphere_volume = (4/3) * 3.14 * (sphere_diameter / 2 / 100)**3  # 구의 부피 계산 (단위: m³)

        # 구의 위치 계산
        if volume >= sphere_volume:  # 완전히 잠긴 경우
            sphere_top = water_level
            sphere_bottom = water_level + sphere_diameter
        else:  # 부분적으로 잠긴 경우
            submerged_ratio = volume / sphere_volume  # 잠긴 부피 비율
            submerged_height = submerged_ratio * sphere_diameter
            sphere_top = water_level - (sphere_diameter - submerged_height)
            sphere_bottom = water_level + submerged_height

        # 구 그리기
        draw_sphere(canvas, water_level, sphere_top, sphere_bottom)

        # 메시지 표시
        result_message = f"부력: {buoyancy_force:.2f} N"
        messagebox.showinfo("결과", result_message)
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자 값을 입력하세요.")

def reset():
    """
    입력 필드와 캔버스 초기화 함수
    """
    entry_density.delete(0, tk.END)
    entry_volume.delete(0, tk.END)
    canvas.delete("all")

# 캔버스 생성
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# 계산 버튼 생성
button_calculate = tk.Button(root, text="계산", command=on_calculate)
button_calculate.pack()

# 원상복구 버튼 생성
button_reset = tk.Button(root, text="원상복구", command=reset)
button_reset.pack()

# 메인 루프 실행
root.mainloop()
