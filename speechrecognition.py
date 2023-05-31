import pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition

engine=pyttsx3.init()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Time now is")
    speak(Time)

  

def date():
    year=int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)
   


def wishme():
    speak("Welcome back Divya!")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    time()
    date()  
    speak("How Can I help You?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source)


def bye():
    speak("Thank you.")
    hour=datetime.datetime.now().hour
    if hour>12:
        speak("Good Night! See you soon")  
         
wishme()
bye()