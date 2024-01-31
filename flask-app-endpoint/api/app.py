from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books", methods=["GET"])
def book_search():
    url_api = os.getenv("BOOK_API_URL")
    response = requests.get(url_api)
    data = response.json()

    query = request.args.get("query")
    filter = request.args.get("filter")

    if query and filter:
        filtered_data = [i for i in data if str(i[filter]) == query]
        return render_template("books.html", results=filtered_data)
    
    return render_template("books.html", results=data)