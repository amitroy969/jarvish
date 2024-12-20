import requests
import json
import pyttsx3
from voice import speak
def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e948fbc8fd7a44fea51cb3484d5f4bb4"
      }

    content = None
    url = None
    print("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    speak("Which field news do you want]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found") 
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

