from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    import random as rand
    num = rand.randint(0, 100)
    return render_template("about.html", kale="This is a random generator: {}".format(num))

if __name__ == '__main__':
    app.run(debug=True)