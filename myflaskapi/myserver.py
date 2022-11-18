
#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("form.html")


def trivia():
    if request.method == "POST":
        if request.form.get("answer"):
            answer = request.form.get("anwer")
            if answer.lower() == "lebron james":
                return render_template("correct.html")
            else:
                return render_template("form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)




