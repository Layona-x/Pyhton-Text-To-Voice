from gtts import gTTS 
import os

d = open("konus.txt","r")
text_d = d.read().replace("/n"," ")
tts = gTTS(text=text_d, lang='tr')
tts.save("hay.mp3")
d.close()
os.system("start hay.mp3")
