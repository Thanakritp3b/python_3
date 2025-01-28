from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Go to path</p>"


@app.route("/<int:id1>/<int:id2>")
def test_square(id1, id2):
    return f"<p>Answer is { id1 ** 2 + id2 ** 2 }<p>"