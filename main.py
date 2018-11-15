import os, requests, time
from bs4 import BeautifulSoup
from gtts import gTTS
url = 'https://www.wunderground.com/health/us/ca/berkeley/94701'
request = requests.get(url)
msg = BeautifulSoup(request.text)

while not msg.find(text='200'):
    time.sleep(30)
    request = requests.get(url)
    if request.status_code != 200:
        print('error getting aqi')
        break
    msg = BeautifulSoup(request.text)
    os.system('cls')
    print('aqi still not over 200 :(')

tts = gTTS(text="AQI is over 200! berkeley is cancelled", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")
