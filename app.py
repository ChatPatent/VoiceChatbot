
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import speech_recognition as sr

#可以录音
def extract_text_from_voice():
  speech_recognition = sr.Recognizer()
  with sr.Microphone() as source:
    audio = speech_recognition.listen(source, phrase_time_limit=2)
    audio_text = ""
    try:
      audio_text = speech_recognition.recognize_google(audio)
      print(audio_text)
    except Exception as e:
      print("Exception: " + str(e))
    return audio_text

extract_text_from_voice()
#可以录音

import openai

#complete = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

import pyttsx3

engine = pyttsx3.init()
#engine.say("Hello Text")
#engine.runAndWait()

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def interact_with_ChatGPT():
    global messages
  
    while True:
        user_text = extract_text_from_voice()
        messages.append({"role": "user", "content": user_text})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = response.choices[0].message.content
        engine.say(reply)
        engine.runAndWait()
        messages.append({"role": "assistant", "content": reply})
        if "Thank you for your time" in reply or "Thank you" in user_text:
            break

# Time to call the function
print("Say something…")
interact_with_ChatGPT()


