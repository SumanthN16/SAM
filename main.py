import datetime
import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import subprocess
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Has Occurred Boss."


if __name__ == '__main__':
    print('PyCharm')
    say("Hello Boss, I am SAM AI")
    while True:
        print("Listening Boss...")
        query = takecommand()
        sites = [["Youtube", "https://youtube.com"], ["Google", "https://google.com"], ["GitHub", "https://github.com/SumanthN16"],]
        for site in sites:
            if f" Open {site[0]}".lower() in query.lower():
                say(f"Okay Boss Opening {site[0]}")
                webbrowser.open(site[1])
        # if "play" or "youtube" or "Music" or "Songs" or "help" in query.lower():


        if "Open Music".lower() in query.lower():
            musicPath = "C:/Users/suman/Downloads/goodmorning.mp3"
            os.system(f"start {musicPath}")
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Boss the time is {strfTime}")
        if "open camera" in query.lower():
            # os.system(f"start C:/Windows/System32/Camera/Camera.exe")
            subprocess.run(['start microsoft.windows.camera:'])