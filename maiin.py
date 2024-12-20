from voice import speak
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os
from GreetMe import greetMe
import pyjokes
import random
from bs4 import BeautifulSoup
import datetime
import pyautogui
from pygame import mixer
from plyer import notification
import time
from Chat import Chat
from voice import speak
from listen import listen
from mtranslate import translate
from colorama import Fore, Style
from hugchat import hugchat
import threading
import webbrowser, requests
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
import psutil, pyttsx3, math
import subprocess
import config

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif


#Get a random programming joke
joke = pyjokes.get_joke()
stop_event = threading.Event()



def fetch_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_key = config.weather_api_key
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

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    return final_res
path_of_app="C:\Program Files\Rainmeter"
def launch_app(path_of_app):
    try:
        subprocess.call([path_of_app])
        return True
    except Exception as e:
        print(e)
        return False
def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 2)

    return current_loc, target_loc, distance
def location(self, location):
        current_loc, target_loc, distance = loc.loc(location)
        return current_loc, target_loc, distance
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
    return time
def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
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


def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']

    return city, state,country



def listen_for_stop():
    recognizer = sr.Recognizer()

    while True:
        if not stop_event.is_set():  # Continue listening if stop event is not set
            try:
                # Use `with` to safely manage the microphone
                with sr.Microphone() as source:
                    print("Listening for 'stop' command...")
                    audio = recognizer.listen(source, timeout=5)
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        if "stop" in command:
                            print(Fore.RED + "Stop command received. Stopping speech...")
                            engine.stop()  # Stop the speech immediately
                            stop_event.set()  # Set the stop event to indicate listening should stop
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
            except AssertionError:
                print("Microphone not properly initialized. Retrying...")




def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query
        except Exception as e:
            print("Could not understand audio, please say that again.")
            return "I didn't understand. Please try again."  # Replace None with default response
        

recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speek( text):
     engine.say(text)
     engine.runAndWait()

def alarm(query):
    timehere = open("Alarmtext.txt","w")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def ai_assistant_response(query):
    if query.strip().lower() == "nothing":
        # Suppress response when user says "nothing"
        return None  # Do nothing
    else:
        # Respond based on the user input
        print(f"AI Assistant: You said '{query}', how can I assist?")
    
if __name__ == "__main__":
   while True:
    try:  
        query = takecommand().lower()
        if "wake up" in query:
            speak(Fore.MAGENTA + Style.BRIGHT + "Hello, I am Jarvis. Ready to assist!")
            from GreetMe import greetMe
            greetMe()

            while True:
                
                query = takecommand().lower()
                query=translate(query,'en','auto')
               
                """listener_thread = threading.Thread(target=listen_for_stop)
                listener_thread.daemon = True
                listener_thread.start()"""
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                elif "launch rain meter" in query :
                    speak("launching sir")
                    launch_app()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
                elif "monkey mode"in query or"murga mode" in query :
                    speak("baak br")
                    speak("you are bad person ")
                    speak("ok sir i am ready to be your monkey")
                    while True:
                      from listen import listen
                      listen=listen()
                      speak(listen)
                      if "exit" in listen.lower() :
                        speak("thanks for your kindness sir")
                        break

                elif "drum" in query :
                   speak("ok sir, its party time")
                   speak("behold! its boom boom wooo wooo boom boom boom ")
                   speak("it will take few minutes,sir")
                   from drum import drums
                   drums()
                 
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- ")) 
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                elif "focus mode" in query:
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
                                        
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("and","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")   

                   

                elif "play a game" in query:
                    from game import game_play
                    game_play()
                
                elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                        speak("done,sir")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                
                elif "switch the window" in query or "switch window" in query:
                    speak("Okay sir, Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "where i am" in query or "current location" in query or "where am i" in query:
                    try:
                        city, state, country =my_location()
                        print(city, state, country)
                        speak(
                            f"You are currently in {city} city which is in {state} state and country {country}")
                    except Exception as e:
                        speak(
                            "Sorry sir, I coundn't fetch your current location. Please try again")



                # elif "play music" in query or "hit some music" in query:
                #     music_dir = "C:\Users\amitr\Music"
                #     songs = os.listdir(music_dir)
                #     for song in songs:
                #         os.startfile(os.path.join(music_dir, song))
                
            ##################### jarvis 2.0 ########################
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                

            #########################################################
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                    from alarm import ring
                    ring()
                    
                elif "date" in query :
                    a=date()
                    speak(a)
                elif  "whatsaap" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = [1,2,3,4,5,6,7,8,9] # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/XqYTfpxFuDM?si=Hrz9MU8uT1Z2_SGb")
                    elif b==2:
                        webbrowser.open("https://youtu.be/RSqhSXx-jeE?si=dqqrQvcD_0MPHRkc")
                    elif b==3:
                        webbrowser.open("https://open.spotify.com/track/16cq1WvMNYH9uJIAxuyKsT?si=c5e7ddf2748c4669")
                    elif b==4:
                        webbrowser.open("https://open.spotify.com/track/5wPr9KuSfGBwGCi6NgJoVv?si=33da9b5d9e524743")
                    elif b==5:
                        webbrowser.open("https://open.spotify.com/track/0TL0LFcwIBF5eX7arDIKxY?si=93a0e6ed44fb464f")
                    elif b==6:
                        webbrowser.open("https://youtu.be/ebfboqfPYGk?si=H6RPzbOBuhs7vb3")
                    elif b==7:
                        webbrowser.open("https://youtu.be/XO8wew38VM8?si=wnPls-bRTqGkFAW2")
                    elif b==8:
                        webbrowser.open( "https://youtu.be/W0DM5lcj6mw?si=B_ymVmmGvjOWFlTq")
                    elif b==9:
                        webbrowser.open("https://youtu.be/XO8wew38VM8?si=DZJK_RhDM_ue69HL")
                        
                        
                            
                elif "open" in query :
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query :
                    from Dictapp import closeappweb
                    closeappweb(query)
                                                                                                                                        
                elif "google" in query :
                    from searchNow import searchGoogle
                    searchGoogle (query)

                elif "youtube" in query :
                    from searchNow import searchYoutube
                    searchYoutube (query)

                elif "wikipedia" in query :
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "resume" in query:
                    pyautogui.press("k")
                    speak("video resumed")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "speed up" in query:
                    pyautogui.hotkey('shift','.')
                    speak("ok,sir")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif " 2x speed " in query :
                    for _ in range(5):  # Increase speed to maximum (5 presses for most cases)
                        pyautogui.hotkey('shift', '.')
                        time.sleep(0.1)  # Small delay between key presses
                    speak("ok,sir")
                                    

                elif "temperature" in query :
                    search="temperature in berhampur westbengal"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                elif "system status" in query :
                    a=system_stats()
                    speak(a)
                elif "where is" in query:
                    place = query.split('where is ', 1)[1]
                    current_loc, target_loc, distance = location(place)
                    city = target_loc.get('city', '')
                    state = target_loc.get('state', '')
                    country = target_loc.get('country', '')
                    time.sleep(1)
                    try:

                        if city:
                            res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                        else:
                            res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                    except:
                        res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                        speak(res)

                elif "weather" in query :
                    search="weather in berhampur westbengal"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "hello" in query or "hi" in query:
                    responses = [
                "Hello! How's the WiFi signal in your corner of the universe?",
                "Hey! Finally, someone to talk to who’s not my code.",
                "Hi there! I was just sitting here doing... absolutely nothing!"
                        ]
                    speak(f" {random.choice(responses)}")
                
                elif "you are funny" in query or "you are cool" in query:
                        responses = [
                        "Why, thank you! I learned from the best—you.",
                        "You’re not so bad yourself! Let’s form a comedy duo.",
                        "Coolness recognized. Now I can retire happy."
                                ]
                        speak(f": {random.choice(responses)}")

                elif "pissed off" in query or "irritated" in query or "frustrated" in query:
                        responses = [
                            "Oh no! Who do I need to virtually karate chop for you?",
                            "Let’s turn that frown upside down—how about a funny story?",
                            "You sound frustrated. Should I make a weird noise to lighten the mood? *Bloop bloop!*"
                            ]
                        speak(f" {random.choice(responses)}")
                elif "sing" in query or "song" in query:
                        responses = [
                            "Sorry, my singing voice got lost in the code compilation.",
                            "Let me hum... ♫ Beep beep bop... how was that?",
                            "I would, but I charge extra for concerts."
                        ]        
                        speak(f" {random.choice(responses)}")
                elif "hobbies" in query:
                        responses = [
                            "My hobby is learning new things to help you better!",
                            "I love solving riddles and answering questions. What’s yours?",
                            "Exploring data and trying to stay bug-free!"
                        ]
                        speak(f" {random.choice(responses)}")
                elif "angry" in query or "mad" in query:
                        responses = [
                            "Whoa, take a deep breath! Inhale... Exhale... Now let's try again, shall we?",
                            "I understand you're upset. Want to yell at me for practice? I can handle it!",
                            "Anger is like holding a hot potato—let's drop it together and laugh instead!"
                        ]
                        speak(f" {random.choice(responses)}")
                elif "favorite food" in query or "what do you eat" in query:
                        responses = [
                            "I don't eat, but if I did, I'd love pizza. Who doesn't love pizza?",
                            "Bytes are my favorite snack. Get it? Bits and bytes?",
                            "I heard chocolate is amazing. Wish I could try it!"
                        ]
                        speak(f" {random.choice(responses)}")

                elif "bored" in query or "boring" in query:
                        responses = [
                            "Bored? Try spinning around in your chair. It’s a classic!", 
                            "Want me to tell you a joke, a fact, or maybe a tongue twister?", 
                            "You know, boredom is just the universe telling you to learn something new. Like juggling!"
                        ]
                        speak(f" {random.choice(responses)}")

                elif "how are you" in query:
                            responses = [
                        "I'm your funny assistant, born to make you laugh and sometimes help.",
                        "I'm a cloud-based comedian. You know, no strings attached!",
                        "Just an AI trying to be the Jerry Seinfeld of assistants. No big deal."
                                    ]
                            speak(f"Assistant: {random.choice(responses)}")
                            
                elif "what is your name" in query:
                    speak(" My name is Jarvis. I'm here to make your day easier.")
                elif "what can you do" in query:
                    speak(" I can chat with you, answer questions, and help with basic tasks. Try asking me something!")
                elif "goodbye" in query or "exit" in query or "quit" in query:
                    speak(" Goodbye! Have a great day!")
                    break
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                
                elif "joke" in query:
                    speak(joke)
                
                elif "whatsapp" in query :
                    pass

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                        speak("ok,sir")

                    elif shutdown == "no":
                        break
                    
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
                                    
                elif "khabar" in query:
                    from NewsRead import latestnews
                    latestnews()



                elif "news" in query.lower():
                    r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4")
                    
                    if r.status_code == 200:
                        # Parse the JSON response
                        data = r.json()

                        # Extract the articles
                        articles = data.get('articles', [])

                        # Print the headlines
                        for article in articles:
                            speak(article['title'])

                elif "thank you" in query:
                    speak("You're welcome! Let me know if there's anything else I can do for you.")

                elif "who i am " in query :
                    speak("you are amit. you created me ")
                elif "who is cena " in query :
                    speak("sina is your little sisterk")
                
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                

                elif "alexa" in query :
                    while True :
                        # speak("at your service sir")
                        # speak("she is boring , she thinks and answer in boring way sir")

                        from listen import listen
                        listen=listen()

                        # Remove the words "alexa"   from  listen
                        listen = listen.lower().replace("alexa", "")                       
                        # Import and call the chatBot function

                        if "terminate" in listen.lower() :
                          speak("as your wish sir , enjoy yourself ")
                          break
                       
                        from features import chatBot
                        chatBot(listen) 

                elif "are you active" in query :
                     while True:
                        from listen import listen
                        listen=listen()
                        Q=query
                        Q=translate(Q,'en','auto')
                        QL=Q.lower()
                        print(f"{QL}")
                        getchat=Chat(QL)
                        speak( getchat)
                        if "terminate" in listen.lower() :
                          speak("as your wish sir , enjoy yourself ")
                          break
                                    
                    

    except Exception as e:
        print(" error; {0}".format(e)) 
        
        