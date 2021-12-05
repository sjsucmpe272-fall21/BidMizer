from flask import Flask, render_template, request
import pandas as pd
from flask_mysqldb import MySQL
from model.bidMizerModel import bidMizerModel
import locale
import os

current_directory = os.getcwd()

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'b95d910e52bbd2'
app.config['MYSQL_PASSWORD'] = 'f81c2328'
app.config['MYSQL_DB'] = 'heroku_8bff76882597e52'
mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')


@app.route('/home', methods=['GET'])
def apphome():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        cur = mysql.connect.cursor()
        query = "select email,password from Account where email='{}' and password='{}'".format(email, password)
        result = cur.execute(query)

        if result:
            query = "select * from Account where email='{}';".format(email)
            cur.execute(query)
            ans = cur.fetchall()

            query = "select * from Projects where email='{}';".format(email)
            cur.execute(query)
            projects = {}
            temp = cur.fetchall()
            for index, p in enumerate(temp):
                project = {'email': p[0], 'name': p[1], 'cost': p[2]};
                projects[index] = project
            cur.close()

            result = {}
            result['firstname'] = ans[0][0]
            result['lastname'] = ans[0][1]
            result['phone'] = ans[0][2]
            result['email'] = ans[0][3]

            return render_template('home.html', result=result, projects=projects)
        else:
            cur.close()
            print("wrong credentials")
            return render_template('login.html')


    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    return render_template('logout.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        phone = request.form.get("phone")
        email = request.form.get("email")
        password = request.form.get("password")

        conn = mysql.connect
        cur = conn.cursor()
        query = "insert into heroku_8bff76882597e52.Account(firstname,lastname,phone,email,password) values('{}','{}','{}','{}','{}');".format(
            firstname, lastname, phone, email, password)
        print(cur.execute(query))
        conn.commit()
        cur.close()

        return render_template('login.html')

    else:
        return render_template('signup.html')


@app.route('/selectProject', methods=['POST'])
def selectProject():
    result = {'email': request.form.get('email')}
    return render_template('selectProject.html', result=result)


@app.route('/predictProject', methods=['POST'])
def predictProject():
    project = request.files['file']
    name = request.form.get('projectname')
    email = request.form.get('email')

    X_predict = pd.read_csv(project, usecols=['Quantity']).values.reshape(1, -1)
    model = bidMizerModel(current_directory)
    modelFit = model.predict(X_predict)
    predCost = locale.currency(modelFit)
    lowRange = modelFit - percentage(10, float(modelFit))
    highRange = modelFit + percentage(10, float(modelFit))
    lowRange = locale.currency(lowRange)
    highRange = locale.currency(highRange)

    conn = mysql.connect
    cur = conn.cursor()
    # Uncomment below lines for adding project into project database
    query = "insert into heroku_8bff76882597e52.Projects(email,projectname,cost) values('{}','{}','{}');".format(email, name,
                                                                                                   predCost)
    cur.execute(query)
    conn.commit()
    cur.close()

    return render_template('predictProject.html', predCost=predCost, lowRange=lowRange, highRange=highRange)

def percentage(percent, whole):
  return (percent * whole) / 100.0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, threaded=True)
