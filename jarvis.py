import pyttsx3
# text into speech 
engine = pyttsx3.init()


engine.say("Hello World")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Friday")

def write(script):
    engine.say(script)
    engine.runAndWait()

write("Hi Sri Divya")

#changing voices 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate =90
engine.setProperty('rate',newVoiceRate)
def write(script):
    engine.say(script)
    engine.runAndWait()

write("Hi Sri Divya")
write("Hi Rajee ...Go sleep")

