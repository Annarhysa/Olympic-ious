from flask import Flask, render_template, request

app = Flask(__name__)

class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
             return self.option1
        elif self.correctOption == 2:
            return self.option2


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    value = request.form['option']
    return value

if __name__ == "__main__":
    app.run(debug=True)