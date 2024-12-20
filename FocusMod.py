import ctypes
import sys
import time
import datetime
import os

# Check if the script has admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def focus_mode(stop_time):
    # Focus mode with admin check, blocking/unblocking websites.
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'
    website_list = [
        'www.facebook.com', 'm.facebook.com',
        'www.instagram.com', 'm.instagram.com',
        'www.twitter.com', 'm.twitter.com',
        'www.linkedin.com', 'm.linkedin.com',
        'www.snapchat.com', 'm.snapchat.com',
        'www.pinterest.com', 'm.pinterest.com',
        'www.tumblr.com', 'm.tumblr.com',
        'www.youtube.com', 'm.youtube.com', 'youtube-nocookie.com',
        'www.whatsapp.com', 'web.whatsapp.com',
        'www.quora.com', 'www.amazon.com', 'm.amazon.com',
        'www.ebay.com', 'm.ebay.com', 'www.alibaba.com', 'm.alibaba.com'
    ]

    # If not admin, restart the script with admin rights
    if not is_admin():
        print("You need to run this script as administrator.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # Block websites
    try:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"{redirect} {website}\n")
                    print(f"Blocked: {website}")

        print("Focus mode is now active!")

        # Calculate the focus time and simulate focus time duration
        start_time = datetime.datetime.now().strftime("%H:%M")
        a = float(start_time.replace(":", "."))
        b = float(stop_time.replace(":", "."))
        focus_duration = round(b - a, 3)

        print(f"Focus mode will run for {focus_duration} hours.")

        time.sleep(focus_duration * 3600)  # Focus time in seconds

        # Unblock websites
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Websites are unblocked and focus mode is over.")

    except PermissionError:
        print("Permission denied! Please run this script as administrator.")

def set_focus_time():
    # Prompt user to input the stop time.
    stop_time = input("Enter stop time (example: 10:10): ").strip()
    return stop_time

def main():
    # Main function to handle user interaction and start focus mode.
    stop_time = set_focus_time()  # Ensure this is inputted first

    # Check if we have admin rights before proceeding
    if not is_admin():
        print("You need to run this script as administrator.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # Once we have the stop time, call the focus mode function and pass the stop_time
    focus_mode(stop_time)

if __name__ == "__main__":
    main()

