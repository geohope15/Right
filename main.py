
from flask import Flask , render_template, request, jsonify

app = Flask(__name__)

@app.route("/partners")
def partners():
    return render_template("partners.html")
	
@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/")
def home():
    return render_template("index.html")

@app.roue("howitwork")
def howitwork():
    return render_template("howitwork.html")

@app.route("/unitowin")
def unitowin():
    return render_template("unitowin.html")

@app.route("/wintouni")
def wintouni():
    return render_template("wintouni.html")

@app.route("/wintozawgyi")
def wintozawgyi():
    return render_template("wintozawgyi.html")
	
@app.route("/zawgyitowin")
def zawgyitowin():
    return render_template("zawgyitowin.html")

@app.route("/zawgyitouni")
def zawgyitouni():
    return render_template("zawgyitouni.html")

@app.route("/unitozawgyi")
def unitozawgyi():
    return render_template("unitozawgyi.html")

if __name__ == "__main__":
    app.run(debug=True)

