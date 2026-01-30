import mss
import numpy as np
import serial
import time
import serial.tools.list_ports

# ====== НАСТРОЙКИ ======
BAUD_RATE = 115200
SMOOTHING = 0.5       # 0 = мгновенно, 1 = очень медленно
MIN_BRIGHT = 20        # минимальная яркость (даже на темных сценах)
MAX_BRIGHT = 120       # максимальная яркость на ленте
BOOST_FACTOR = 1.2     # коэффициент усиления цвета
SLEEP_TIME = 0.04      # ~25 FPS

# ====== АВТОПОИСК ESP32 ======
def find_esp32_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB' in p.description or 'UART' in p.description:
            return p.device
    return None

port = find_esp32_port()
if port is None:
    print("ESP32 не найден! Подключи и попробуй снова.")
    exit(1)

ser = serial.Serial(port, BAUD_RATE)
time.sleep(2)  # пауза для инициализации
print(f"ESP32 найден на {port}")

# ====== ИНИЦИАЛИЗАЦИЯ ======
r_f = g_f = b_f = 0

# ====== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ======
def scale_color(val):
    """Приводим цвет в диапазон MIN_BRIGHT-MAX_BRIGHT"""
    val = max(val, MIN_BRIGHT)       # минимальная базовая яркость
    val = min(val, 255)              # верхний предел исходного цвета
    val = int(val / 255 * MAX_BRIGHT) # масштабируем под MAX_BRIGHT
    return val

def boost(val):
    """Усиливаем цвет, но не выше MAX_BRIGHT"""
    return min(int(val * BOOST_FACTOR), MAX_BRIGHT)

# ====== ГЛАВНЫЙ ЦИКЛ ======
with mss.mss() as sct:
    monitor = sct.monitors[1]  # основной экран

    while True:
        img = np.array(sct.grab(monitor))

        # усреднение цветов по экрану
        b = img[:, :, 0].mean()
        g = img[:, :, 1].mean()
        r = img[:, :, 2].mean()

        # масштабирование и минимальная яркость
        r_scaled = scale_color(r)
        g_scaled = scale_color(g)
        b_scaled = scale_color(b)

        # усиление цвета
        r_scaled = boost(r_scaled)
        g_scaled = boost(g_scaled)
        b_scaled = boost(b_scaled)

        # сглаживание
        r_f = r_f * SMOOTHING + r_scaled * (1 - SMOOTHING)
        g_f = g_f * SMOOTHING + g_scaled * (1 - SMOOTHING)
        b_f = b_f * SMOOTHING + b_scaled * (1 - SMOOTHING)

        # отправка на ESP32
        data = f"{int(r_f)},{int(g_f)},{int(b_f)}\n"
        ser.write(data.encode())

        time.sleep(SLEEP_TIME)
