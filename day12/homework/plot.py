from flask import Flask, request, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)

def plot_graph(x_form, x_to, graph_type):
    x = np.linspace(x_form, x_to, 100)
    if graph_type == 'sin':
        y = [np.sin(i) for i in x]
    elif graph_type == 'cos':
        y = [np.cos(i) for i in x]
    elif graph_type == 'square':
        y = [i**2 for i in x]
    elif graph_type == 'sqrt' :
        y = [np.sqrt(i) for i in x]
    plt.plot(x, y)
    plt.savefig('static/plot.png')
    plt.close()
    return 'static/plot.png'



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/plot", methods=['POST'])
def plot():
    x_form = float(request.form['x_form'])
    x_to = float(request.form['x_to'])
    graph_type = request.form['graph_type']
    print(graph_type)
    plot_url = plot_graph(x_form, x_to, graph_type)
    return render_template('index.html', plot_url=plot_url)