from urllib import request
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=number, yyy=current_year)


@app.route('/guess/<name>')
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}")
    data = age.json()
    print(data)
    number = data["age"]
    return f"Name = {name} <br> guess age = {number}"


@app.route("/blog")
def get_blog():
    blog_url = "https://newsdata.io/api/1/news?apikey=pub_36746622dac086aa325d928a2a39e1e4b8d4&country=in"
    response = requests.get(blog_url)
    all_posts = response.json()
    data = all_posts['results']

    return render_template('blog.html', posts=data)


if __name__ == "__main__":
    app.run(debug=True)
