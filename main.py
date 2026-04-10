from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def detect_mood(text):
    
    score = TextBlob(text).sentiment.polarity
    if score > 0.2:
        return "Happy"
    elif score < -0.2:
        return "Stressed"
    else:
        return "Neutral"

def recommend_task(mood):
    if mood == "Happy":
        return "Creative or teamwork tasks"
    elif mood == "Neutral":
        return "Routine or documentation tasks"
    else:
        return "Light tasks or take a break"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form.get("name")
        text = request.form.get("text")

        if text:
            mood = detect_mood(text)
            task = recommend_task(mood)
            result = {
                "name": name,
                "mood": mood,
                "task": task
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=False)
