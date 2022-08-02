import googletrans
import speech_recognition as sr

recognizer = sr.Recognizer()
translator = googletrans.Translator()

try:
    with sr.Microphone() as source:
        print('Speak Now')
        recognizer.adjust_for_ambient_noise(source)#(Problem Solved)
        voice= recognizer.listen(source)
        text= recognizer.recognize_google(voice)
        print(text)

except:
     pass

translated = translator.translate(text, dest='es')
print(translated.text)