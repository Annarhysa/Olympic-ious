import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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

if __name__ == "__main__":
    app.run(debug=True)
