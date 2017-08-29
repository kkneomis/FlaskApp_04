from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    favorite_character = "Jon Snow"
    others = ["Danny", "The hound", "Arya", "Night King"]
    return render_template("index.html",
                           favorite_character = favorite_character,
                           others = others)


if __name__ == '__main__':
    app.run()
