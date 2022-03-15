import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os 

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("rate",178)

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

if __name__ == '__main__':
    speak(" Namaste Tarun Sir")
    speak("Loki assistance activated ")
    speak("How can i help you  sir")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'who are you' in query:
            speak("I am Loki developed by Tarun Kumar")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'open mail' in query:
            speak("opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open bb ki vines' in query:
            speak("opening bb ki vines")
            webbrowser.open("https://www.youtube.com/c/BBKiVines")
        elif 'open r2h' in query:
            speak("opening R2H")
            webbrowser.open("https://www.youtube.com/c/Round2hell")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("C://Users\DELL\Desktop\WhatsApp.lnk")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'loki tell me time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)
        elif 'open kgf teaser' in query:
            speak("opening local disk D")
            webbrowser.open("C://Users\DELL\Videos\kgf teaser.mp4")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'shutdown loki' in query:
            speak("okay thank you  sir")

            exit(0)
