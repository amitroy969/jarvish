import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from voice import speak
"""engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  """

#dictapp = { "Microsoft Edge": "Microsoft Edge", "Microsoft Store": "Microsoft Store", "Calculator": "Calculator", "Calendar": "Calendar", "Camera": "Camera", "Mail": "Mail", "Weather": "Weather", "Xbox": "Xbox", "OneDrive": "OneDrive", "Notepad": "Notepad", "WordPad": "WordPad", "Photos": "Photos", "Paint": "Paint", "Groove Music": "Groove Music", "Movies & TV": "Movies & TV", "Snipping Tool": "Snipping Tool", "Sticky Notes": "Sticky Notes", "Alarms & Clock": "Alarms & Clock", "Windows Security": "Windows Security", "Settings": "Settings", "Bing": "Bing", "Office 365": "Office 365", "LinkedIn": "LinkedIn", "Skype": "Skype", "OneNote": "OneNote"}
dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}


def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query or  "the tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak(" tab closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs closed")
    else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")


         




























































