from flask import Flask, render_template

# the template folder is for all the html templates
# and the static folder is for all static files like  images,music ,videos,css , js

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
