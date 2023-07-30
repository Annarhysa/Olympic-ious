from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)

#class for questions of quiz
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

q1 = Question(1, "In which city were the first modern Olympic Games held in 1896?", "Athens, Greexe", "Rome, Italy", "London, United Kingdom", 1)
q2 = Question(2, "Which athlete has won the most gold medals in Olympic history?", "Michael Phelps", "Katie Ledecky", "Usain Bolt", 1)
q3 = Question(3, "Which city has hosted the most Olympic Games?", "London, UK", "Bejin, Japan", "Paris, France", 1)
q4 = Question(4, "In which sport did the 'Miracle on Ice' take place during the 1980 Winter Olympics?", "Ice Skating", "Volleyball", "Ice Hockey", 3)
q5 = Question(5, "Which Olympic sport involves gliding down a track while lying on a small sled?", "Bosleigh", "Luge", "Skeleton", 3)
q6 = Question(6, "Which legendary athlete won four gold medals in the 1936 Berlin Olympics and shattered Adolf Hitler's myth of Aryan supremacy?", "Jesse Owens", "Usain Bolt", "Carl Lewis", 1)
q7 = Question(7, "In which year were women allowed to participate in the modern Olympics for the first time?", "1900", "1920", "1936", 1)

questions_list = [q1, q2, q3, q4, q5, q6, q7]





#route to quiz page
@app.route("/quiz", methods = ['POST', 'GET'])
def quiz():
    return render_template("quiz.html", questions_list = questions_list)




#route to score display page
@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    correct_count = 0
    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count = correct_count+1
    
    if (correct_count>=0 and correct_count<=4):
        compliment = "Better Luck Next Time"
    elif (correct_count>=5 and correct_count<=6):
        compliment = "Wow, Not Bad!"
    elif(correct_count>6):
        compliment = "You must be a genius"
    
    correct_count = str(correct_count)
    statement = correct_count+"/7"

    facts = ["Ancient 'Naked' Olympics: In ancient Greece, athletes competed in the nude. The word 'gymnasium' comes from the Greek word 'gymnos,' meaning naked.",
             "Jesse Owens' Triumph: African-American athlete Jesse Owens won four gold medals in the 1936 Berlin Olympics, disproving Adolf Hitler's theory of Aryan racial superiority.",
             "London's Three-Time Host: London, England, has hosted the Olympics three times (1908, 1948, and 2012), making it the only city to do so.",
             "The 1964 Tokyo Olympics were the first held in Asia, and the 2008 Beijing Olympics were notable for being held at high altitude, affecting some endurance events.",
             "In recent Olympics, efforts have been made to use environmentally friendly materials. For instance, the medals at the 2020 Tokyo Olympics were made from recycled electronic devices.",
             "In the 1900 Paris Olympics, there was an event called 'live pigeon shooting,' where contestants shot at live pigeons released from traps. Over 300 birds were killed, leading to outrage, and the event was never repeated.",
    ]

    return render_template("exit.html", score = statement, compliment = compliment, fact = random.choice(facts))




#route to home page
@app.route("/olympicious")
def summary():
    return render_template("index.html")



#route to olympics history page
@app.route("/summary", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        country_name = request.form['country'].strip().title()
        if country_name:
            stats = get_olympic_stats(country_name)
            url = images(country_name)
            if stats:
                return render_template("summary.html", stats=stats, country=country_name, file = url)
            else:
                return render_template("error.html")
            
#function to get the summary from csv file
def get_olympic_stats(country_name):
    with open("data/Olympics_summary.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["\ufeffcountry_name"] == country_name:
                summary = row["summary"]
                return summary
            
#fucntion to add images of countries
def images(country_name):
    country = country_name.lower()
    data = {
        'united states of america': 1, 'russia': 2, 'china': 3, 'germany':4, 'great britain':5, 'australia':6, 
        'japan': 7, 'france': 8, 'italy': 9, 'brazil': 10}
    
    keys = data.keys()

    for n in keys:
        if n == country:
            value = data[n]
            image_map = {
                1: 'assets/usa.jpeg',
                2: 'assets/Russia.jpg',
                3: 'assets/china.jpg',
                4: 'assets/germany.jpg',
                5: 'assets/gb.jpg',
                6: 'assets/australia.webp',
                7: 'assets/japan.webp',
                8: 'assets/france.jpg',
                9: 'assets/itlay.jpg',
                10: 'assets/brazil.jpg',}
            image_filename = image_map.get(value)
            return image_filename
    

#route to show top 10 countries graphs
@app.route("/stats", methods=['POST', 'GET'])
def new():
    return render_template("stats.html")


#main
if __name__ == "__main__":
    app.run(debug=True)