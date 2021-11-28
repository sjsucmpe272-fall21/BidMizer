from flask import Flask, render_template, request
import pandas as pd
from model.bidMizerModel import bidMizerModel
import locale
import os
current_directory = os.getcwd()

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html');

@app.route('/home', methods=['GET'])
def apphome():
    return render_template('home.html');

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html');

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('logout.html');

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html');

@app.route('/selectProject', methods=['GET'])
def selectProject():
    return render_template('selectProject.html');

@app.route('/predictProject', methods=['POST'])
def predictProject():
    project = request.files['file']
    X_predict = pd.read_csv(project, usecols=['Quantity']).values.reshape(1, -1)
    model = bidMizerModel(current_directory)
    predCost = locale.currency(model.predict(X_predict))
    return render_template('predictProject.html', predCost=predCost);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, threaded=True)
