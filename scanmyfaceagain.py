import sys
from fer import FER
import os
import time
import matplotlib.pyplot as plt 
import pyttsx3 
import speech_recognition as sr
import sys, os

from functools import lru_cache
isenabled = True
lru_cache(maxsize=10000)

img = plt.imread("image.png")
detector = FER(mtcnn=True)
point = detector.top_emotion(img)
plt.imshow(img)
print(point)
roro = pyttsx3.init('sapi5')
voices = roro.getProperty('voices')
roro.setProperty('voice',voices[1].id)
from functools import lru_cache
lru_cache(maxsize=100)

def speak(audio):
    roro.say(audio)
    roro.runAndWait()
    lru_cache(maxsize=500, typed=True)



def angry():
    speak("you still look angry lol")
    speak("you got anger issues ?")
    speak("you need to work on that mate")
   
    
#__________________________________________________________________________________#


def disgust():
        speak("you have that disgusting look on the face")
        speak("eeeeeeeeeeewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        speak("damn go out and chill with your fur ends")
        speak("did you fart ..........brrr..... sure you did lol")

#__________________________________________________________________________________#

def fear():
        speak("You seem pretty afraid with something")
        speak("Do you need an help ?")
        speak("is there anything i could do ?")
        speak("dont be a coward...")
#__________________________________________________________________________________#

def sad(): 
        speak("You seem pretty sad..")
        speak("what's up!!")
        speak("hey i'm your friend i can help you with anything")
        speak("you can tell me anything you know that right?")
        speak("Every thing is gonna be alright.. eh !!")
#__________________________________________________________________________________#

def surprise():
        speak("hey, pal you look suprised with something")
        speak("what is it ?")
        speak("let me make your day..")
        speak(" just hang on with me for a min")
#__________________________________________________________________________________#

def happy():
        speak("uuwwwuuu.. some one looks happy today")
        speak("well guess who it is ?")
        speak("it's you my man")
        speak ("how can i help you today")
#__________________________________________________________________________________#

def neutral():
        speak("seems you had a lazy day mate")
        speak("rise and sunshine")
        speak("put of that lazy face ... common mate you got thing to do")
        speak("you look cute tho..hihihihihihi")
        
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
