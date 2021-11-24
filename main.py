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

@app.route('/selectProject', methods=['GET'])
def selectProject():
    return render_template('selectProject.html');

@app.route('/predictProject', methods=['POST'])
def predictProject():
    project1 = current_directory + "/projects/project1.csv"
    X_predict = pd.read_csv(project1, usecols=['Quantity']).values.reshape(1, -1)
    model = bidMizerModel(current_directory)
    predCost = locale.currency(model.predict(X_predict))
    return render_template('predictProject.html', predCost=predCost);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, threaded=True)
