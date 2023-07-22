from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Sample quiz questions and answers
quiz_questions = [
    {
        'question': 'Which city hosted the 2020 Summer Olympics?',
        'options': ['Tokyo', 'Beijing', 'London', 'Rio de Janeiro'],
        'correct_answer': 'Tokyo'
    },
    {
        'question': 'Which country won the most gold medals in the 2016 Summer Olympics?',
        'options': ['USA', 'China', 'Russia', 'Great Britain'],
        'correct_answer': 'USA'
    },
    # Add more questions here
]

# Sample medal tally stats
medal_tally = {
    'USA': {'gold': 39, 'silver': 41, 'bronze': 33},
    'China': {'gold': 38, 'silver': 32, 'bronze': 18},
    'Russia': {'gold': 20, 'silver': 28, 'bronze': 23},
    # Add more countries here
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for question in quiz_questions:
            selected_option = request.form.get(question['question'])
            if selected_option == question['correct_answer']:
                score += 1
        return f'Your score: {score}/{len(quiz_questions)}'
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/medal-tally')
def medal_tally_page():
    return render_template('medal_tally.html', medal_tally=medal_tally)

if __name__ == '__main__':
    app.run(debug=True)
