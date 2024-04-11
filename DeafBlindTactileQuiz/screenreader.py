from bs4 import BeautifulSoup
import pyttsx3
import os
from gtts import gTTS

def fetch_text(template, li_flag = False):
    with open("temp.html", "w") as f:
        f.write(template)
    soup = BeautifulSoup(open('temp.html'), 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    text += ' '.join([l.get_text() for l in soup.find_all('li')])
    print("TEXT: ", text)
    return text

def read_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def main(template):
    text = fetch_text(template)
    read_text(text)
    return 0

def generate_mp3(template, output_mp3, li_flag = False):
    # generate mp3 from text
    text = fetch_text(template, li_flag = li_flag)
    temp_obj = gTTS(text=text, lang='en', slow=False)
    temp_obj.save("static/" + output_mp3)
