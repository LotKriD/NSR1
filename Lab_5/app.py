from flask import Flask, render_template, request, url_for, redirect
import json
import os

dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, 'data.json')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def hello():
    return 'HELLO!'

@app.route('/data/categories', methods = ['GET', 'POST'])
def render_categories():
    if request.method == "POST":
        category = request.form['category']
        return redirect(url_for('render_category', category = category))

    data = []
    for i in temp['categories']:
       data.append(temp['categories'][str(i)]['category'])

    return render_template('categories.html', data = data)

@app.route('/data/categories/<category>')
def render_category(category):
    data = []
    data.append(category)
    data.append("{}: ".format(category))

    c_id = 0
    for i in temp['categories']:
        if temp['categories'][str(i)]['category'] == category:
            c_id = i
            break

    for i in temp['product']:
        if temp['product'][str(i)]['category_id'] == str(c_id):
            data.append("{}: {}. Price - {}".format(i, temp['product'][str(i)]['product'], 
            temp['product'][str(i)]['price']))

    return render_template('category.html', data = data)

@app.route('/data/product', methods = ['GET', 'POST'])
def render_products():
    if request.method == "POST":
        product = request.form['product']
        id = 0
        for i in temp['product']:
            if temp['product'][str(i)]['product'] == product:
                id = i
        return redirect(url_for('render_product', id = id))

    data = []
    for i in temp['product']:
       data.append("{}: {}".format(i, temp['product'][str(i)]['product']))

    return render_template('data.html', data = data)

@app.route('/data/product/<int:id>')
def render_product(id):
    data = []
    data.append(temp['product'][str(id)]['product'])
    data.append("Категория: {}".format(temp['categories'][temp['product'][str(id)]['category_id']]['category']))
    data.append('Товар: {}'.format(temp['product'][str(id)]['product']))
    data.append('Цена: {}'.format(temp['product'][str(id)]['price']))

    return render_template('product.html', data = data)

if __name__ == '__main__':
    with open(data_path) as f:
       temp = json.load(f)
       
    app.run()