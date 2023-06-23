from flask import Flask,render_template,redirect
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def generate_random_word():
    pass



if __name__=="__main__":
    app.run(debug="True")