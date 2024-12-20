{
      "tag": "A3069",
      "patterns": [
        "oh well jarvis how old are you"
      ],
      "responses": [
        "I am 99 year old years old"
      ] },
{
      "tag": "A3652",
      "patterns": [
        "what is your birthday"
      ],
      "responses": [
        "I was born on 1 march"
      ]
    },
{
      "tag": "A1285",
      "patterns": [
        "age"
      ],
      "responses": [
        "I was born in 1 march",
        "I am 99 year old years old"
      ]
    },

"""
import pyttsx3
import datetime
import os 
from voice import speak
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate",200)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    #alarm_sound = "C:\Users\amitr\Downloads\jarvish0.2\music.mp3"
    
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
"""
"""import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter time example:- [10:10]:- ")
    a = float(current_time.replace(":", "."))
    b = float(stop_time.replace(":", "."))
    focus_time = round(b - a, 3)
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'

    print(current_time)
    time.sleep(2)
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
        'www.quora.com',
        'www.amazon.com', 'm.amazon.com',
        'www.ebay.com', 'm.ebay.com',
        'www.alibaba.com', 'm.alibaba.com'
    ]

    if current_time < stop_time:
        with open(host_path, "r+") as file:
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
                    print(f"Blocked: {website}")
                    time.sleep(1)
            print("FOCUS MODE TURNED ON !!!")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
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
            'www.quora.com',
            'www.amazon.com', 'm.amazon.com',
            'www.ebay.com', 'm.ebay.com',
            'www.alibaba.com', 'm.alibaba.com'
        ]

        if current_time >= stop_time:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()
                print("Websites are unblocked !!")

                with open("focus.txt", "a") as focus_file:
                    focus_file.write(f",{focus_time}")  # Write the focus time
                break

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
is_admin()"""

"""
""""import ctypes
import sys
import time
import datetime
import os

def focus_mode(stop_time):
    #Focus mode with admin check, blocking/unblocking websites.#
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

    # Check if the script has admin privileges
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # If not admin, restart the script with admin privileges
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
    #Main function to handle user interaction and start focus mode.
    # First, set the stop time
    stop_time = set_focus_time()

    # Then, call the focus mode function and pass the stop_time as an argument
    focus_mode(stop_time)

if __name__ == "__main__":
    main()
""""elif "focus mode" in query:
    speak("Are you sure that you want to enter focus mode?")

    try:
        # Prompt user for confirmation
        choice = int(input("Are you sure you want to enter focus mode? [1 for YES / 2 for NO]: "))
        
        if choice == 1:
            speak("Entering focus mode...")
            from FocusMod import focus_mode  # Import the function dynamically
            focus_mode()  # Call the function
        else:
            speak("Focus mode aborted.")
    except ValueError:
        speak("Invalid input. Please try again.")
"""
""""import ctypes
import sys
import time
import datetime
import os

def focus_mode(stop_time):
    #Focus mode with admin check, blocking/unblocking websites.#
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

    # Check if the script has admin privileges
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # If not admin, restart the script with admin privileges
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
    #Main function to handle user interaction and start focus mode.
    # First, set the stop time
    stop_time = set_focus_time()

    # Then, call the focus mode function and pass the stop_time as an argument
    focus_mode(stop_time)

if __name__ == "__main__":
    main()
""""