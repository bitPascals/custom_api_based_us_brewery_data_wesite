from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)

bootstrap = Bootstrap(app)

parameters = {
    "page": 12,
    "per_page": 4
}

response = requests.get("https://api.openbrewerydb.org/v1/breweries/")
results = response.json()


@app.route("/")
def home():
    all_results = results
    return render_template("index.html", breweries=results)


if __name__ == "__main__":
    app.run(debug=False)
