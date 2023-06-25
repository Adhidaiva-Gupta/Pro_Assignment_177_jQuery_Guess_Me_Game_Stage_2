from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)


# #templates is the array of all the words with the number of inputs 
# each word will have, the category and the actual word.
templates = [
    {
        "inputs": 5,
        "category": "Sports",
        "word": "Chess"
    },

    {
        "inputs": 6,
        "category": "The Name of a European Country",
        "word": "France"
    },

]

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/get-template")
def get_template():
        return jsonify({
                "status": "success",
                "word": random.choice(templates)
        })
