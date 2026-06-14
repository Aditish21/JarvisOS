import psutil
import pyautogui
from datetime import datetime

def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        return f"Battery: {battery.percent}%"
    return "battery information unavailable"

def get_ram():
    ram = psutil.virtual_memory()
    return f"RAM Usage: {ram.percent}%"

def get_cpu():
    return f"CPU Usage:{psutil.cpu_percent()}%"

def take_screenshot():

    filename = (
        f"screenshot_"
        f"{datetime.now().strftime('%H%M%S')}.png"
    )

    screenshot = pyautogui.screenshot()

    screenshot.save(filename)

    return f"Screenshot saved as {filename}"