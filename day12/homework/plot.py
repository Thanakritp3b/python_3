from flask import Flask, request, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)

def plot_graph(x_form, x_to, graph_types, color,seperate):
    if len(graph_types) <= 1:
        seperate = '0'
    if seperate == '1':   
        fig, axs = plt.subplots(len(graph_types), 1, figsize=(8, 6))
    x = np.linspace(x_form, x_to, 100)
    for i, graph_type in enumerate(graph_types):
        y = generate_y_values(x, graph_type)
        if seperate == '1':
            axs[i].plot(x, y, color=color, label=graph_type)
            axs[i].set_title(graph_type)
            axs[i].set_xlabel('x')
            axs[i].set_ylabel('y')
            axs[i].set_ylim(-3, 3)
            axs[i].grid(True)
        else:
            plt.plot(x, y, color=color, label=graph_type)
    plt.tight_layout()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.savefig('static/plot.png')
    plt.close()
    return 'static/plot.png'


def generate_y_values(x, graph_type):
    if graph_type == 'sin':
        return np.sin(x)
    elif graph_type == 'cos':
        return np.cos(x)
    elif graph_type == 'square':
        return x**2
    elif graph_type == 'sqrt':
        return np.sqrt(np.abs(x))
    else:
        return x



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/plot", methods=['POST'])
def plot():
    x_form = float(request.form['x_form'])
    x_to = float(request.form['x_to'])
    color = request.form['color']
    graph_types = request.form.getlist('graph_type[]') if 'graph_type[]' in request.form else [request.form.get('graph_type')] 
    seperate = (request.form.get('seperate'))
    print(seperate)
    print(graph_types)
    plot_url = plot_graph(x_form, x_to, graph_types,color,seperate)
    return render_template('index.html', plot_url=plot_url)