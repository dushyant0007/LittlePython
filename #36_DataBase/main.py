from contextlib import nullcontext
from datetime import timedelta
from crypt import methods
import imp
import re
from this import d
from flask import Flask, render_template, url_for, request, session, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(seconds=10)

#  dataTable is the name of the db table
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataTable.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_object = SQLAlchemy(app)


class users(db_object.Model):
  def __init__(self, name, password):
    self.name = name
    self.password = password
  _id = db_object.Column(db_object.Integer, primary_key=True)
  name = db_object.Column(db_object.String(250), unique=True, nullable=False)
  password = db_object.Column(db_object.String(250), nullable=False)



    # #Optional: this will allow each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f'<Book {self.title}>'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        session["d_data"] = data
        user = users(session["d_data"]["email"], session["d_data"]["password"])
        found_user = users.query.filter_by(name=user.name).first()
        if found_user:
              return redirect(url_for('user_already_exist'))
        else:    
          db_object.session.add(user)
          db_object.session.commit()
          return redirect(url_for("ok"))
    else:
        return render_template("login.html")


@app.route('/ok')
def ok():
    return render_template("ok.html")


@app.route("/logout")
def logout():
    # session.pop("d_data", None)
    # None is message associate with removing that data
    return redirect(url_for("home"))


@app.route("/view")
def view():
    return render_template("view.html",all_data=users.query.all())


@app.route("/user_already_exist")
def user_already_exist():
    return render_template("user_already_exist.html")

if __name__ == "__main__":
    db_object.create_all()  # going to create db if not exist
    app.run(debug=True)
