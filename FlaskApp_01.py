from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/main/<user>')
def main(user):

    return render_template("index.html", username=user)


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/processform', methods=['GET', 'POST'])
def processform():
    user = request.form['user']
    return redirect(url_for('main', user=user))

if __name__ == '__main__':
    app.run()
