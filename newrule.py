from fer import FER
import os
import time
import matplotlib.pyplot as plt 
import random 
import json 
import pickle
from sys import maxsize
import numpy as np 
import nltk 
from nltk.stem import WordNetLemmatizer
from regex import W
import tensorflow
import pyttsx3 
import speech_recognition as us 
import selenium

from selenium import webdriver as wd 
from functools import lru_cache
isenabled = True
lru_cache(maxsize=10000)
import tensorflow
from tensorflow.keras.models import load_model
import pywhatkit as kit



#__________________________________________________________________________#

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.h5')
roro = pyttsx3.init('sapi5')
voices = roro.getProperty('voices')
roro.setProperty('voice',voices[1].id)

#______________________________________________________________________________#
def speak(audio):
    roro.say(audio)
    roro.runAndWait()
    lru_cache(maxsize=500, typed=True)

#__________________________________________________________________________________#
def cleanScentence(sentence):
    sentence_words =nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
#__________________________________________________________________________________#

def bagwords(sentence):
    sentence_words = cleanScentence(sentence)
    bag = [0]* len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
#__________________________________________________________________________________#

def Wikipedia():
    speak("wikipedia is enabled")
    while(True):
        speak("what's your query")
        u = us.Recognizer()
        u.energy_treshold = 2000
        with us.Microphone() as source:
                u.parse_treshold =100
                audio = u.listen(source)
                fact = new_func(u, audio)
                if(fact == "exit" or fact == "quit"):
                    return 0 
                else:
                    msg = kit.info(fact,lines=2)
                    time.sleep(6)
                    speak(msg)
#___________________________________________________________________________________#

import requests

def weather():
    city = input('Ballari')
    print(city)
    print('Displaying Weater report for: ' + city)
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    speak(res.text)
    return(res.text)

#__________________________________________________________________________________#
def predictclass(sentence):
    bow = bagwords(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_TRESHOLD = 0.25
    result = [[i,r]for i, r in enumerate(res) if r > ERROR_TRESHOLD]
    result.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for r in result:
        return_list.append({'intent':classes[r[0]],'probablity':str(r[1])})
    return return_list

#__________________________________________________________________________________#

def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']
    listofintents = intents_json['intents']
    for i in listofintents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

#__________________________________________________________________________________#

def musicalhits():
    speak("Name your favourite music")
    while(True):
        u = us.Recognizer()
        u.energy_treshold = 2000
        with us.Microphone() as source:
                u.parse_treshold =100
                audio = u.listen(source)
                fact = new_func(u, audio)
                if(fact == "exit" or fact == "quit"):
                    return 0 
                else:
                    fact= u.recognize_google(audio,language ='en-us')
                    kit.playonyt(fact)
#__________________________________________________________________________________#

def new_func(u, audio):
    fact =  u.recognize_google(audio,language ='en-us')
    return fact
#__________________________________________________________________________________#

def google_chrome():
    while(True):
        speak("What do you wanna search for")
        u = us.Recognizer()
        u.energy_treshold = 2000
        with us.Microphone() as source:
                u.parse_treshold =100
                audio = u.listen(source)
                fact = new_func(u, audio)
                if(fact == "exit" or fact == "quit" or fact == "close`"):
                    return 0 
                else:
                    driver = wd.Chrome()
                    fact= u.recognize_google(audio,language ='en-us')
                    driver.get('https://www.google.com/search?q={}'.format(fact))    

#__________________________________________________________________________________#

def playgames():
    speak("Comming Up.. Games")
    speak("Opening Games")
    while(True):
        speak("i have games of snakes and ping pong")
        u = us.Recognizer()
        u.energy_treshold = 2000
        with us.Microphone() as source:
                u.parse_treshold =100
                audio = u.listen(source)
                fact = new_func(u, audio)
                if(fact == "exit" or fact == "quit" or fact == "close"):
                    return 0 
                elif(fact == "snakes" or fact=="snake"):
                    import snakes
                    snakes()
                    
                else:
                    fact= u.recognize_google(audio,language ='en-us')
                    speak("sorry can't find {} game in this section".format(fact))


def chess():
    loopers = 0
    while(loopers>0):
        driver = wd.Chrome()
        driver.get("https://www.chess.com/play/online") 


#__________________________________________________________________________________#

def introspeak():
    isenabled = True
    loopr = 2 
    for i in range(loopr):
        u = us.Recognizer()
        u.energy_treshold = 5000
        with us.Microphone() as source:
            speak("what do you wanna do today ?")
            speak("i have features of chrome, wikipedia, chess and music")
            speak("choose one")

            u.parse_treshold =100
            audio = u.listen(source)
        try:
            speak("processing...")
            message= u.recognize_google(audio,language ='en-us')
            print(message)
        except Exception as e:
            speak("come again")


        ints= predictclass(message)
        res = get_response(ints, intents)
        speak(res)
        if(message == "Wiki" or message == "Wikipedia"):
            Wikipedia()
        elif(message == "Chrome"):
                google_chrome()
        elif(message == "chess" or "Chess"):
                chess()
        elif(message == "play music"):
                musicalhits() 
        elif(message == "play games"):
            playgames()

        elif(message == "weather" or message=="Weather"):
            weather()

        
        elif(message == "quit" or message == "exit"):
            isenabled = False
        else:
            os.remove("Img0.jpg")
            break
    
#__________________________________________________________________________________#
    
introspeak()
