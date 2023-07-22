from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/quiz")
def quiz():
    return "Test quiz"

if __name__ == "__main__":
    app.run(debug=True)