import os
import openai
from config import apikey
from openai import OpenAI


client = OpenAI(api_key = apikey)

response = client.completions.create(
  model="davinci-002",
  prompt="write a letter",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
