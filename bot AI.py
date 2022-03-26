import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

print("jagernaout")
MASTER = "Farhan ganteng"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
#kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
#jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        talk("Hello Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        talk("Hello Good Afternoon" + MASTER)
    else:
        talk("Haello Good Evening" + MASTER)

def take_command():
    try:
        with sr.Microphone() as source:
            print("mendengarkan")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                print(command)
                command = command.replace("jarvis", "")
                talk(command)
                
    except:
        pass

    return command


def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("playing"+ song)
        print("playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("time now is "+ time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("searching wikipedia")
        print(info)
        talk(info)
    else:
        talk("not any intruction")
        print(command)
wishMe()

while True:   
    MASTER = "Farhan ganteng"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    #kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    #jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    talk("I am jagernaout what do you want")
    run_jarvis()