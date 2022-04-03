import googletrans
import speech_recognition as sr
import sys
import json
import requests

recognizer = sr.Recognizer()
translator = googletrans.Translator()

try:
    with sr.Microphone() as source:
        print('Speak Now')
        recognizer.adjust_for_ambient_noise(source,duration=1)#(Problem Solved)
        voice= recognizer.listen(source)
        text= recognizer.recognize_google(voice)
        # text="hii"
        text=text.json()
       

except:
     pass
# text={"human":"hii","assistant":"hello"}
r=json.dumps(text)
q=json.loads(r)
print(type(q))
# translated = translator.translate(text, dest='hi')
# print(translated.text)
sys.stdout.flush()