import os
import subprocess
import keyboard
import time

def toggle_rainmeter():
    """Toggles Rainmeter on or off."""
    rainmeter_exe = "C:\\Program Files\\Rainmeter\\Rainmeter.exe"

    try:
        # Check if Rainmeter is running
        process_list = subprocess.check_output('tasklist', shell=True, text=True)
        if "Rainmeter.exe" in process_list:
            os.system('taskkill /f /im Rainmeter.exe')  # Kill Rainmeter
        else:
            subprocess.Popen(rainmeter_exe)  # Start Rainmeter
    except Exception as e:
        print(f"Error: {e}")

print("Press Ctrl+Alt+R to toggle Rainmeter. Press Esc to exit.")

while True:
    try:
        # Listen for hotkey
        if keyboard.is_pressed("ctrl+alt+r"):
            toggle_rainmeter()
            time.sleep(0.5)  # Prevent rapid toggling
        elif keyboard.is_pressed("esc"):
            print("Exiting...")
            break
    except KeyboardInterrupt:
        break
