import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from dotenv import load_dotenv
load_dotenv()
chrome_path = "C://Users//Singh//AppData//Local//Google//Chrome//Application//chrome.exe %s"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" Good Morning!")

    elif hour>=12 and hour<18:
        speak(" Good Afternoon!")

    else:
        speak(" Good Evening!")

    speak(" This is your honey . Tell me how can I help you ")
     
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv("email"),os.getenv("password"))
    server.sendmail(os.getenv("email"),to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

# logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'open bootstrap' in query:
            webbrowser.get(chrome_path).open("getbootstrap.com")

        elif 'open classroom' in query:
            webbrowser.get(chrome_path).open("classroom.google.com")

        elif ' open chef' in query:
            webbrowser.get(chrome_path).open("codechef.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Ma'am , The time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to unnati' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = os.getenv("email")
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email at this particular moment")    