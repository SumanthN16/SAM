import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from openai import OpenAI
from config import apikey
import subprocess
import datetime
import random
speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatstr =""
def chat(qurey):
    global chatstr
    client = OpenAI(api_key=apikey)
    chatstr += f"User: {qurey}\n Jarvis: "

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response)
    # todo: wrap this inside of a try catch block
    # print(response.choices[0].text)
    say(response.choices[0].text)
    chatstr += f"{response.choices[0].text}\n"

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)
    return response.choices[0].text


def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************\n\n"
    client = OpenAI(api_key=apikey)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response)
    # todo: wrap this inside of a try catch block

    text += response.choices[0].text
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)


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

        # apps=[["Open Music, "]]
        if "Open Music".lower() in query.lower():
            musicPath = "C:/Users/suman/Downloads/goodmorning.mp3"
            os.system(f"start {musicPath}")
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Boss the time is {strfTime}")
        elif "open camera" in query.lower():
            # os.system(f"start C:/Windows/System32/Camera/Camera.exe")
            subprocess.run(['start microsoft.windows.camera:'])

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        else:
            chat(query)