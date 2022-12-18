
import requests  ## This module take url of website
import random    ## use of random module to shuffle news every time
import json       ## To access or load the content of news
from newsapi import newsapi_client


def speaker(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__=='__main__':
    # speak("I am a boy")
    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=e2d65163e5404176bfb1bf66201d2568")
    News = json.loads(r.content)   ##News is a dictionary
    main = News["articles"]  ##main is a list
    random.shuffle(main)   ##shuffling of list to get differnt news at every time


    i=1
    for articles in main:
        print(i)
        speaker(str(i))
        print(articles['title'],"\n",articles['url'])
        speaker(articles['title'])
        i=i+1








