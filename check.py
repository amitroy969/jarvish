from voice import speak
import datetime
import  eel
import re
import os
import random
import pprint
import requests
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_MainWindow
import config
from listen import listen
import requests
import config
import eel


def fetch_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_key = "01c8e8ed152b5c7789bf4ee94a8dae19"
    units_format = "&units=metric"
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key + units_format

    response = requests.get(complete_url)

    city_weather_data = response.json()

    if city_weather_data["cod"] != "404":
        main_data = city_weather_data["main"]
        weather_description_data = city_weather_data["weather"][0]
        weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]

        final_response = f"""
        The weather in {city} is currently {weather_description} 
        with a temperature of {current_temperature} degree celcius, 
        atmospheric pressure of {current_pressure} hectoPascals, 
        humidity of {current_humidity} percent 
        and wind speed reaching {wind_speed} kilometers per hour"""

        return final_response

    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again"
def weather(self, city):
        self.city=city
        """
        Return weather
        :param city: Any city of this world
        :return: weather info as string if True, or False
        """
        try:
            res = fetch_weather(city)
        except Exception as e:
            print(e)
            res = False
        return res

def Time():
    """
    Just return time as string
    :return: time if success, False if fail
    """
    try:
        time = datetime.datetime.now().strftime("%H:%M:%S")
    except Exception as e:
        print(e)
        time = False
def startup():
    speak("Initializing Jarvis")
    # speak("Starting all systems applications")
    # speak("Installing and checking all drivers")
    # speak("Caliberating and examining all the core processors")
    # speak("Checking the internet connection")
    # speak("Wait a moment sir")
    # speak("All drivers are up and running")
    # speak("All systems have been activated")
    # speak("Now I am online")
    # hour = int(datetime.datetime.now().hour)
    # if hour>=0 and hour<=12:
    #     speak("Good Morning")
    # elif hour>12 and hour<18:
    #     speak("Good afternoon")
    # else:
    #     speak("Good evening")
    # c_time =Time()
    # speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def date():
    """
    Just return date as string
    :return: date if success, False if fail
    """
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    return date

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = Time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
#if __name__ == "__main__":

@eel.expose
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        wish()

        while True:
            command = listen()

            if re.search('date', command):
                date = date()
                print(date)
                speak(date)

            elif "jarvis friend" in command :
                speak("ok sir ")
                speak("initionalizing jarvis 2.0")
                speak("he is sleeping sir, wwhould you want me to give him a kik in his ass")
                speak("as you wish")
                
            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res =weather(self,city=city)
                print(weather_res)
                speak(weather_res)

            # elif "play music" in listen or "hit some music" in listen:
            #         music_dir = "C:\\Users\\amitr\\Music\\jarvy1"
            #         songs = os.listdir(music_dir)
            #         for song in songs:
            #             os.startfile(os.path.join(music_dir, song))
            elif "time" in command:
                time_c = Time()
                print(time_c)
                speak(f"Sir the time is {time_c}")
            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()
                
startExecution = MainThread()

@eel.expose
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

  
@eel.expose
def run_check():
    print("Button clicked, executing check functionality from check.py")
    startExecution = MainThread()
    app = QApplication(sys.argv)
    jarvis = Main()
    jarvis.show()
    exit(app.exec_())
    # You can add whatever code you need to run when the button is clicked here
    # For example, let's say we want to print a message to confirm it's working:
    print("Executing the check operation!")
    # You can add more functionality as needed

# # Start the Eel app
# eel.init('web')  # Specify your web folder (frontend files like HTML, JS)
# eel.start('index.html', size=(800, 600))  # Adjust according to your frontend requirements


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

#run_check()
