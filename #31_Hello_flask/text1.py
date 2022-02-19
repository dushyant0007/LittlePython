from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


# <name> // name is variable which user going to type in url
@app.route('/<name>')
def greet(name):
    return f'Hello {name}'


# int is the datatype
@app.route('/<name>/<int:number>')
def into(name, number):
    return f'Hello {name} and my age {number}'


if __name__ == '__main__':
    app.run(debug=True)
