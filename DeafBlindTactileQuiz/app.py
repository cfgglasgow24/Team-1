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
    sr.main(render_template('quiz.html', options=options, question=question, captions=captions))
    return render_template('quiz.html', options=options, question=question, captions=captions)


if __name__ == '__main__':
    app.run()
