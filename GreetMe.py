import speech_recognition as sr
import pyttsx3
import datetime
from voice import speak
"""recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak( text):
     engine.say(text)
     engine.runAndWait()
"""
def  greetMe ():
     hour=int(datetime.datetime.now().hour)
     if hour >=0 and hour <=12 :
          speak("GOOD morning,sir")
     elif hour >12 and hour <=17 :
          speak("GOOD afternoon,sir")
     else :
          speak("GOOD evening,sir")
     #speak("please tell me, How can help you ?")    























