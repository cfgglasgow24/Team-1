from flask import Flask, render_template
import screenreader as sr
import quiz as q

app = Flask(__name__, )


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/quiz/")
def quiz():
    contextdict = q.quiz()
    question = contextdict["correct letter"]
    options = contextdict["random letters"]
    captions = [contextdict["captions"][options[0]], contextdict["captions"][options[1]]]
    rendered_page = render_template('quiz.html', options=options, question=question, captions=captions)
    sr.generate_mp3(rendered_page, "quiz_audio.mp3")
    return rendered_page


if __name__ == '__main__':
    app.run()
