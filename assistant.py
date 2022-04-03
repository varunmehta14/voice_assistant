import googletrans
import speech_recognition as sr
import sys
import json
import requests

recognizer = sr.Recognizer()
translator = googletrans.Translator()

try:
    with sr.Microphone(device_index = 0) as source:
        print('Speak Now')
        recognizer.adjust_for_ambient_noise(source,duration=3)#(Problem Solved)

        voice= recognizer.listen(source)
        print(recognizer.recognize_google(voice))
        text= recognizer.recognize_google(voice)
       
        results={"text":text}
       
except:
     pass
# text={"human":"hii","assistant":"hello"}
# r=json.dumps(text)
# q=json.loads(r)
# print(str(q))
# translated = translator.translate(text, dest='hi')
# print(translated.text)
# print(text)
# results={"text":text}
# print(str(results))