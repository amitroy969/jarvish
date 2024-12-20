import pyttsx3
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',165)
engine.setProperty('voice',voices[1].id)
#brian1,+1emma2+1,griant3+1,janifer4+1,raveena5+1,russel6+1,salli7+1,amy10+1
for i in voices:
   print(i.id)

def speak (*args,**kwargs):
    audio=""
    for i in args:
        audio +=str(i)
        print(Fore.CYAN+audio)
        engine.say(audio)
        engine.runAndWait()
#speak()
#speak("hello my name is jarvis and i am a creation of tony stark")
#speak("“We cannot solve problems with the kind of thinking we employed when we came up with them.by —Albert Einstein")

