#!/usr/bin/env python3
import requests
import json
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import time
#response = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=10").text
response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").text
#print(response.json())
dict_obj = json.loads(response)
print("Display Title: ", dict_obj.get('displaytitle'))
print("Page Title: ", dict_obj.get('titles'))
print("Page ID : ", dict_obj.get('pageid'))
print("Description : ", dict_obj.get('description'))
print("-----------Main Content---------- \n", dict_obj.get('extract'), " ", dict_obj.get('extract_html'))
text = f"Display Title: {dict_obj.get('titles')} Page Title: {dict_obj.get('pageid')}, Description : {dict_obj.get('description')}, Main Content : {dict_obj.get('extract')} {dict_obj.get('extract_html')}"
gTTSobject = gTTS(text)
gTTSobject.save('random.mp3')
sound = AudioSegment.from_mp3('random.mp3')
play(sound)
