from flask import Flask,render_template
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/home')
def home():
    return render_template("home.html")

fortune_list=["Great opportunities await you in the near future. Stay alert and be ready to seize them.",
"A journey of a thousand miles begins with a single step. Take that first step with confidence.",
"Your creativity and hard work will soon be recognized and rewarded.",
"Unexpected financial gains are coming your way. Prepare wisely.",
"Love and happiness will surround you this year. Embrace it with an open heart.",
"Challenges will test your resilience, but they will also strengthen your character.",
"A new friendship will bring joy and positivity into your life.",
"Health and vitality will be your allies in achieving your goals this season.",
"Trust your instincts in making decisions; they will lead you in the right direction.",
"Generosity towards others will bring you inner peace and fulfillment."]

@app.route('/furtune_telling')
def furtune():
    fortune = fortune_list[random.randint(0,9)]
    return render_template("furtune.html", f = fortune)



    
if __name__ == '__main__':
    app.run(debug=True)