import pyttsx3
import datetime
import os
import time

def ring(file_path="Alarmtext.txt"):
    try:
        # Step 1: Read and clean up the alarm time from the file
        with open(file_path, "r") as file:
            alarm_time = file.read().strip()
        with open(file_path, "w") as file:
            file.truncate(0)

        # Step 2: Process and format the alarm time
        alarm_time = (
            alarm_time.lower()
            .replace("jarvis", "")
            .replace("set an alarm", "")
            .replace(" and ", ":")
            .strip()
        )
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
        print(f"Alarm set for: {alarm_time}")

        # Step 3: Loop to wait for the alarm time
        engine = pyttsx3.init("sapi5")
        engine.setProperty("voice", engine.getProperty("voices")[1].id)
        engine.setProperty("rate", 200)

        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= alarm_time:
                # Speak and play alarm sound
                engine.say("Alarm ringing, sir.")
                engine.runAndWait()
                os.startfile("music.mp3")  # Replace with the path to your sound file
                break
            time.sleep(1)  # Wait to prevent high CPU usage
    except FileNotFoundError:
        print("Error: Alarm file not found.")
    except ValueError:
        print("Error: Invalid time format in the alarm file.")
    except Exception as e:
        print(f"An error occurred: {e}")
   
# Run the alarm
ring()









