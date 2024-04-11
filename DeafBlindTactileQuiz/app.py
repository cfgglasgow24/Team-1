from flask import Flask, render_template
import screenreader as sr

app = Flask(__name__, )


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/quiz/")
def quiz():
    question = "A"
    options = ["A", "B"]
    captions = ["The Letter A", "The Letter B"]
    rendered_page = render_template('quiz.html', options=options, question=question, captions=captions)
    sr.generate_mp3(rendered_page, "quiz_audio.mp3")
    return rendered_page


if __name__ == '__main__':
    app.run()
