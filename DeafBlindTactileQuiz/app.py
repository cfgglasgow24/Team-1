from flask import Flask, render_template
import screenreader as sr
import quiz as q

app = Flask(__name__, )


@app.route('/')
def accessibility():
    sr.generate_mp3(render_template('popup.html'), "popup_audio.mp3")
    return render_template('popup.html')


@app.route('/home/')
def home():
    sr.generate_mp3(render_template('home.html'), "home_audio.mp3")
    return render_template('home.html')

@app.route("/quiz/")
def quiz():
    contextdict = q.quiz()
    question = contextdict["correct letter"]
    options = contextdict["random letters"]
    captions = [contextdict["captions"][options[0]], contextdict["captions"][options[1]]]
    sr.generate_mp3(render_template('quiz.html', options=options, question=question, captions=captions), "quiz_audio.mp3")
    return render_template('quiz.html', options=options, question=question, captions=captions)


if __name__ == '__main__':
    app.run()
