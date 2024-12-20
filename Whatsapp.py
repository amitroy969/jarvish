import pywhatkit
import pyttsx3
import speech_recognition
import datetime
import webbrowser
from datetime import datetime
from time import sleep
import os
import bs4
from datetime import timedelta
from voice import speak
"""engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()"""

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
query=takecommand().lower()

def sendMessage():
    
    if "kanha" in query :
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91 9732612901",message,time_hour=strTime,time_min=update)
    elif "aditya" in query :
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91 8092933359",message,time_hour=strTime,time_min=update)
    pass




sendMessage()





















































