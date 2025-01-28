from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def calculate():
    number = int(request.form['number'])
    result = number * number
    return render_template('index.html', number=number, result=result)