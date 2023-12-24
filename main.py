
import speech_recognition as sr
import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Has Occurred Boss."


if __name__ == '__main__':
    print('PyCharm')
    say("Hello Boss, I am SAM AI")
    while True:
        print("Listening...")
        text = takeCommand()
        say(text)

