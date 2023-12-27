from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
# This is a decorator function that runs the below function only if the user is trying to access the main homepage URL.
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

if __name__ == '__main__':
    app.run()