import sys
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
import speech_recognition as sr
import selenium
import sys, os
import pywhatkit

from selenium import webdriver as wd 
from functools import lru_cache
isenabled = True
lru_cache(maxsize=10000)
import tensorflow
from tensorflow.keras.models import load_model
import pywhatkit as kit



#__________________________________________________________________________#

listener = sr.Recognizer()
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

#_______________________________________________________________________________#

speak("Jexi is Up and running !!")
speak("hang onn.. let me scan you")
speak("hello, I'm a neural network bot specially designed to make your day better")
img = plt.imread("image.png")

detector = FER(mtcnn=True)
point = detector.top_emotion(img)
plt.imshow(img)
print(point)

#__________________________________________________________________________________#
def cleanScentence(sentence):
    sentence_words =nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
#__________________________________________________________________________________#

def bagwords(sentence):
    sentence_words = cleanScentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


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




def talkback():
#    speak("listening")
#    with sr.Microphone() as source:

#        voice = listener.listen(source)
#        command = listener.recognize_google(voice)
    command = command.lower()
    print(command)
    speak("How do you feel today")
    speak("give me the input")
    command = input()
    if 'alexa' in command:
        command = command.replace('alexa', '')
        print(command)
    ints = predictclass(command)
    res = get_response(ints,intents)
    speak(res)
    if "yes" in command:
        speak("which genre music you want to hear")
        a = "company justin beiber"
        pywhatkit.playonyt(a)
        print("Playing...+{}".format(a))
    if "exit" in command:
        sys.exit()
    if "egg" in command:
        speak("opening egg game.....")
        os.system("python C:/Users/Ganiiiii/Desktop/cam/catchegg.py")
                    
    if "pacman" in command:
        os.system("python C:/Users/Ganiiiii/Desktop/cam/pacman.py")
    if "snakes" in command:
        os.system("python C:/Users/Ganiiiii/Desktop/cam/snakes.py")
    if 'boat' in command:
        os.system("C:/Users/Ganiiiii/AppData/Local/Apps/2.0/WMCW2PC7.68Y/JDQLOLJB.796/jarv..tion_3c2b46bb851e27cf_0002.0006_238c9011606637a3/jarvisWPF.exe")    
        
        

#_________________________________________________________________________________________#


def angry():
    speak("You seems to be pretty angry today")
    speak("how can i cheer you up!!")
    speak("what do you wanna do ?")
    speak("Just say chess to play chess")
    talkback()

    
#__________________________________________________________________________________#


def disgust():
        speak("you seem disgusted by something")
        speak("Whaddup.. my mate")
        talkback()

#__________________________________________________________________________________#

def fear():
        speak("You seem pretty afraid with something")
        speak("Do you need an help ?")
        speak("is there anything i could do ?")
        talkback()
#__________________________________________________________________________________#

def sad(): 
        speak("You seem pretty sad..")
        speak("what's up!!")
        speak("hey i'm your friend i can help you with anything")
        speak("you can tell me anything you know that right?")
        speak("Every thing is gonna be alright.. eh !!")
        talkback()
#__________________________________________________________________________________#

def surprise():
        speak("hey, pal you look suprised with something")
        speak("what is it ?")
        speak("let me make your day..")
        speak(" just hang on with me for a min")
        talkback()
#__________________________________________________________________________________#

def happy():
        speak("uuwwwuuu.. some one looks happy today")
        speak("well guess who it is ?")
        speak("it's you my man")
        speak ("how can i help you today")
        talkback()
#__________________________________________________________________________________#

def neutral():
        speak("seems you had a lazy day mate")
        speak("rise and sunshine")
        speak("put of that lazy face ... common mate you got thing to do")
        speak("you look cute tho..hihihihihihi")
        talkback()
        
#__________________________________________________________________________________#
    

if(point[0]=='angry'):
    print("angry emotion detected")
    angry()
elif(point[0]=='disgust'):
    print("disgust emotion detected")
    disgust()
elif(point[0]=='fear'):
    print("Fear emotion detected")
    fear()
elif(point[0]=='sad'):
    print("sad emotion detected")
    sad()

elif(point[0]=='surprise'):
    print("surprise emotion detected")
    surprise()
elif(point[0]=='happy'):
    print("happy emotion detected")
    happy()
else:
    print("neutral emotion detected")
    neutral()


while True:
    talkback()
        


