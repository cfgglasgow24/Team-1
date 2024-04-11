import random

from flask import Flask

app = Flask(__name__)


@app.route('/quiz/')
def quiz():
    # Transmit information to HTML file
    random_letters = list(map(str, 32 + random.sample(range(0, 26), 2)))
    
    correct_option = random.randrange(2) # 0 = left, 1 = right
    letter = random_letters[correct_option]
    letter_audio_path = correct_letter + ".mp3"
    
    image_paths = [random_letter + ".png" for random_letter in random_letters]
    # letter_descriptions_and_audio
    
    # Wait
    
    # Receive information from HTML file
    
    EXIT_CODE = 2
    
    if (code_received == EXIT_CODE):
        # GO BACK TO THE MAIN PAGE
    