from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    value = request.form['option']
    return value

if __name__ == "__main__":
    app.run(debug=True)