from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = "Jon Snow"
    return "Hello world! My name is " + name


if __name__ == '__main__':
    app.run()
