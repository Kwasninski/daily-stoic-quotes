from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


# fetch stoic quote
def get_quote():
    url = "https://stoic.tekloon.net/stoic-quote"
    response = json.loads(requests.request("GET", url).text)
    quote = response['data']['quote']
    author = response['data']['author']
    return quote, author

# main page route
@app.route("/")
def index():
    quote,author = get_quote()
    return render_template("stoic_index.html", quote=quote, author=author)
    



if __name__ == "__main__":
    app.run(debug=True)

