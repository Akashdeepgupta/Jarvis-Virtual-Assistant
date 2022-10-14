import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib                  #for sending emails

engine = pyttsx3.init("sapi5")  # to take the user's voice using window's in-built api
voices = engine.getProperty("voices")
# print(voices)         #gives two voices name one male and one female

engine.setProperty("voice", voices[1].id)
# to get female voice give index as 1 and for male it is 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am jarvis sir. Please tell me how may i help you")


def sendEmail(to, content):
    # for sending the email you have to allow the less secure apps in your sending email address
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("akashdeepg2001@gmail.com", "Akash@2001")
    server.sendmail("akashdeepg2001@gmail.com", to, content)
    server.close()


def takeCommand():
    # it takes voice input from user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def showstr(str):
    print("Hello World")
    return str


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(str(result).encode("utf-8"))
            speak(result)
            exit()

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
        
        elif "but why" in query:
            speak("Because there is some issue which i am unable to trace i will learn that")
            exit()

        elif "open vs code" in query:
            speak("opening vs code")
            codePath = "C:\\Users\\Akashdeep Gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath.replace("\\", "\\\\"))
            speak("vs code is opened")
        elif any(map(lambda x:x in query,["mail","email","mail to","send email","send mail","send a mail","send an email"])):
            try:
                speak("What should i say")
                content = takeCommand()
                to = "akashdeepg2001@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry i'm not able to sent the email at the moment")
        elif any(map(lambda x:x in query,["quit","exit","stop","bye","go","go to hell"])):
            exit()

        elif any(map(lambda x:x in query,["photo","open photos","images","open images","show me photos","show me images"])):
            photo_dir = "C:\\Users\\Akashdeep Gupta\\Music\\Musify\\Download" # give the location of folder where your photos is located
            photos = os.listdir(photo_dir)
            print(photos)
            speak("sir Playing music as you said")
            os.startfile(os.path.join(photo_dir, photos[0]))
            exit()
       
        elif "play music" in query:
            music_dir = "C:\\Users\\Akashdeep Gupta\\Music\\Musify\\Download"  # give the location of folder where your song is located
            songs = os.listdir(music_dir)
            print(songs)
            speak("sir Playing music as you said")
            os.startfile(os.path.join(music_dir, songs[0]))
            exit()

      
        else:
            speak("Please say something")