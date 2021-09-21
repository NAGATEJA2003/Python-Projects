import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
speaker = pt.init()

speaker.setProperty('rate',150)


def talk(text):
    speaker.say(text)
    speaker.runAndWait()
    
talk("Hi, These is Personal Voice Assistant using python, How can I help you ?")
print("Things I can doo...")
print("1. Can play song/video in YT : Play song/video name...")
print("2. Can tell time : What is the time...")
print("3. Can give information using Wiki : Search thing/topic name...")
print("4. Can entertain you using jokes : Tell me a joke...")

def talk_command():
    try:
        with sr.Microphone() as source:
            print("Your PVA is Listening.....\nWaiting for your Request")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass

    return command

def run_jarvis():
    command = talk_command()
    print(command)
    
    if('play' in command):
        song = command.replace('play','')
        print("\nplaying"+ song)
        talk("playing"+ song)
        pywhatkit.playonyt(song)
        
    elif('time' in command):
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("\nCurrent time is "+time)
        talk("Current time is "+time)

    elif('search' in command):
        search = command.replace("search","")
        try:
            info = wikipedia.summary(search, 2)
            talk("Searching "+search)
            print("\n"+info)
            talk(info)
            
        except:
            print("Sorry I failed to search",search)
            talk("Sorry I failed to search"+search)

    elif('joke' in command):
        a=pyjokes.get_joke()
        print("\n"+a)
        talk(a)

    elif("" in command):
        print("I cant hear anything from you, Please say it again.")
        talk("I cant hear anything from you, Please say it again.")
    else:
        print("\n"+"I didnt understood your words, Please say it again.")
        talk("I didnt understood your words, Please say it again.")
        
while True:
    run_jarvis()
        

run_jarvis()
