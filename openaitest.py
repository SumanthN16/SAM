import os
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
import openai
from config import apikey
from openai import OpenAI
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
  speaker.Speak(text)


client = OpenAI(api_key = apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="HOW ARE YOU",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].text)
say(response.choices[0].text)
