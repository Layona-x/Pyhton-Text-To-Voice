from gtts import gTTS 
import os
import time

d = open("konus.txt","r")
text_d = d.read().replace("/n"," ")
tts = gTTS(text=text_d, lang='tr')
#Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
tts.save("hay.mp3")
d.close()
#şimdi ise bu dosyayı açalım.
os.system("start hay.mp3")