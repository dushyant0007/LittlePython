from crypt import methods
from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "Hello"

# Session  for long time
# STEP 1
###########
from datetime import timedelta
app.permanent_session_lifetime = timedelta(days=99)
############


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        print(data)
        # return redirect(url_for("demo",usr=data["username"]))

        # with the help of session
        session["sdata"] = data
######################
        # STEP 2
        # session.permanent = True
####################
        print(session)
        return redirect(url_for("demo"))

    else:
        return render_template("login.html")


# @app.route("/<usr>")
# def demo(usr):
#     return f"<p>Name of user is {usr}</p><p>Password of user is </p>"

@app.route("/ok")
def demo():
    if "sdata" in session:
        data = session["sdata"]
        print(data)
    return f"<p>Name of user is {session['sdata']['username']} </p>\
               <p>Password of user is {session['sdata']['password']}</p>"


@app.route("/logout")
def logout():
    session.pop("sdata", None)
    # None is message associate with removing that data

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
