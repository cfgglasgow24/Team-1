from flask import Flask, request
from bs4 import BeautifulSoup
import pyttsx3
import os

app = Flask(__name__)

def fetch_text(template):
    with open("test.html", "w") as f:
        f.write(template)
    soup = BeautifulSoup(open('test.html'), 'html.parser')
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

# if __name__ == "__main__":
#     base = os.path.abspath(os.getcwd())
#     template = base + '/DeafBlindTactileQuiz/templates/quiz.html'
#     main(template=template)