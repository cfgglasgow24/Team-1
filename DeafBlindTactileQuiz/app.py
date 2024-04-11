from flask import Flask, render_template

app = Flask(__name__, )


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route("/quiz/")
def quiz():
    question = "A"
    options = ["A", "B"]
    captions = ["The Letter A", "The Letter B"]
    return render_template('quiz.html', options=options, question=question, captions=captions)


if __name__ == '__main__':
    app.run()
