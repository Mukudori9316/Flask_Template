from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/hello/")
def hello():
    return render_template('hello.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()
