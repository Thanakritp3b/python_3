from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Go to path</p>"


@app.route("/<id1>")
def test_square(id1):
    x=id1.split(',')
    return f"<p>Answer is {int(x[0])**2 + int(x[1])**2}<p>"