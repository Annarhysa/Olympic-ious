from flask import Flask, render_template, request
import csv

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
        elif self.correctOption == 3:
            return self.option3

q1 = Question(1, "What is the Olympic motto in Latin and what does it mean in English?", "Citius, Altius, Fortius (Faster, Higher, Stronger)", "xyz", "abc", 1)
q2 = Question(2, "Which athlete has won the most gold medals in Olympic history?", "Michael Phelps", "Prithvi Shah", "Usain Bolt", 1)
q3 = Question(3, "Which city has hosted the most Olympic Games?", "London, UK", "Bejin, Japan", "Paris, France", 1)
q4 = Question(4, "In which sport did the 'Miracle on Ice' take place during the 1980 Winter Olympics?", "Ice Skating", "Volleyball", "Ice Hockey", 3)

questions_list = [q1, q2, q3, q4]

@app.route("/quiz")
def home():
    if request.method == "POST":
        country_name = request.form['country'].strip().title()
        if country_name:
            stats = get_olympic_stats(country_name)
            if stats:
                return render_template("result.html", stats=stats, country=country_name)
            else:
                return render_template("error.html")
    return render_template("index.html")

def get_olympic_stats(country_name):
    with open("Olympics_summary.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["\ufeffcountry_name"] == country_name:
                summary = row["summary"]
                return summary

def quiz():
    return render_template("quiz.html", questions_list = questions_list)

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    correct_count = 0
    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count = correct_count+1

    correct_count = str(correct_count)

    statement = "Your score is "+correct_count+"/4"

    return statement

if __name__ == "__main__":
    app.run(debug=True)