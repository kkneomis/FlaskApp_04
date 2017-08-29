from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/')
def login():
    return render_template("form.html")


@app.route('/processform', methods=['GET', 'POST'])
def processform():
    song = request.form
    return render_template("index.html", song=song)

if __name__ == '__main__':
    app.run()
