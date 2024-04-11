import random

def quiz():
    # Transmit information to HTML file
    options_storage = dict()
    
    options_storage["random letters"] = list(map(str, 65 + random.sample(range(0, 26), 2)))
    options_storage["left or right"] = random.randrange(2) # 0 = left, 1 = right
    options_storage["correct letter"] = random_letters[options_storage["left or right"]]
    options_storage["correct audio"] = options_storage["correct letter"] + ".mp3"
    
    options_storage["image paths"] = [random_letter + ".jpg" for random_letter in options_storage["random letters"]]
    options_storage["desc and audios"] = [(letter + "_description.txt", letter + "_description_audio.mp3") for letter in options_storage["random letters"]]
    
    return options_storage
