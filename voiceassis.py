import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os 

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("rate",158)

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


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
    speak("somia assistance activated ")
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
            speak("I am  world's most beautiful girl somia which are  programmed by Tarun Kumar ")
        elif 'who is tarun' in query:
            speak("He is an engineering student from pantnagar and he is  my friend ")
        elif 'give me your contact number' in query:
            speak("9389767451")
            print("9389767451")
        elif 'when is your birthday' in query:
            speak("seven december ")
            print("07 december")
        elif 'what is your email id' in query:
            speak("07somiav@gmail.com")
            print("07saumyav@gmail.com")
        elif 'do you have any facebook account' in query:
            speak("no i dont have any facebook account ")
        elif 'do you have any instagram account' in query:
            speak("yes ")
        elif 'tell me your hobbies' in query:
            speak(" my hobbies are dance, enjoy to some new places and what is your hobbies ")
        elif 'tell me the name of your school' in query:
            speak("m square public school and pnf public school pithoragarh , tell me your schools name ")
        elif 'open your childhood photo' in query:
            speak("opening my childhood photo")
            webbrowser.open("E:\ECE ISRO ESE\IMG-20211221-WA0005.jpg")
        elif 'open your photo' in query:
            speak("opening my photo")
            webbrowser.open("E:\ECE ISRO ESE\Screenshot_2022-05-25-21-14-17-341_com.whatsapp.jpg")       
        elif 'give me your insta id' in query:
            speak("opening insta id")
            webbrowser.open("https://www.instagram.com/7saumya_verma/")
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
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("C://Users\DELL\Desktop\WhatsApp.lnk")
        elif 'play phir miloge na song' in query:
            speak("opening song")
            webbrowser.open("https://youtu.be/n0VNjUNjB-g")
        elif 'open college website' in query:
            speak("opening college website")
            webbrowser.open("http://www.gbpuat-tech.ac.in/")
        elif 'open old registered website' in query:
            speak("opening regi ")
            webbrowser.open("http://gbpuat-regi.com/newregi/default.html")
        elif 'somia tell me time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)
        elif 'open kgf teaser' in query:
            speak("opening local disk D")
            webbrowser.open("C://Users\DELL\Videos\kgf teaser.mp4")
        elif 'shutdown somia' in query:
            speak("okay thank you  sir")

            exit(0)
