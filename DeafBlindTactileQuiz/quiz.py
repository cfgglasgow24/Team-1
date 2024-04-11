import random

def quiz():
    # Transmit information to HTML file
    options_storage = dict()
    
    options_storage["random letters"] = list(map(str, 65 + random.sample(range(0, 26), 2)))
    options_storage["left or right"] = random.randrange(2) # 0 = left, 1 = right
    options_storage["correct letter"] = random_letters[options_storage["left or right"]]
    options_storage["correct audio"] = options_storage["correct letter"] + ".mp3"
    options_storage["image paths"] = [random_letter + ".jpg" for random_letter in options_storage["random letters"]]
    
    options_storage["captions"] =   {'A': 'touch the end of their thumb with your right forefinger.',
                                     'B': 'place all your right hand finger tips in the middle of their left palm.',
                                     'C': 'draw your right forefinger down their thumb and along the top of the outstretched forefinger.',
                                     'D': 'place the thumb and forefinger of your right hand (other fingers tucked away) on the forefinger of their left hand.',
                                     'E': 'touch the end of their forefinger with your right forefinger.',
                                     'F': 'place your forefinger and middle finger at right angles to their forefinger and middle finger.',
                                     'G': 'put a fist onto their left hand, small finger down.',
                                     'H': 'smooth your right hand, fingers together, across their left hand.',
                                     'I': 'touch the middle finger of their left hand.',
                                     'J': 'draw the letter “J” down the middle of their left hand.',
                                     'K': 'bend your right forefinger at right angles against their forefinger.',
                                     'L': 'place your right forefinger flat on the palm of their hand.',
                                     'M': 'place your three middle fingers flat on their hand.',
                                     'N': 'place two fingers flat on their hand.',
                                     'O': 'touch the ring finger of their left hand.',
                                     'P': 'pinches their left forefinger using your right forefinger and thumb.',
                                     'Q': 'put your forefinger around the base of their thumb.',
                                     'R': 'place your bent forefinger flat on the palm of their hand.',
                                     'S': 'place your right forefinger between their small finger and ring finger.',
                                     'T': 'place forefinger on their hand at right angles.',
                                     'U': 'your forefinger touches their small finger.',
                                     'V': 'your forefinger and middle finger in a “V” shape on their palm.',
                                     'W': 'place your right hand on their palm then fold fingers over.',
                                     'X': 'place forefinger on top of their forefinger.',
                                     'Y': 'place your forefinger, at the bottom of their thumb.',
                                     'Z': 'place the side of your hand into their left palm.'}
    
    return options_storage
