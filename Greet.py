import pyttsx3
import datetime

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
    time()
    date()
    speak("I am at your service. How can I help you?")

wishme()