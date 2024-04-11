from flask import Flask, render_template
import screenreader as sr

app = Flask(__name__, )


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route("/quiz/")
def quiz():
    question = "A"
    options = ["A", "B"]
    captions = ["The Letter A", "The Letter B"]
    sr.main(render_template('quiz.html', options=options, question=question, captions=captions))
    return render_template('quiz.html', options=options, question=question, captions=captions)


if __name__ == '__main__':
    app.run()
