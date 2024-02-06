from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def apuri():
    return render_template("apuri.html") 

if __name__ == "__main__":
    app.run()