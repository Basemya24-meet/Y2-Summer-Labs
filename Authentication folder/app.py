from flask import Flask,render_template,request,url_for,redirect
import random
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = "secret"




firebaseConfig = {
  "apiKey": "AIzaSyB-BFGvdceb0lSxnRdL7X7zr8ZyOfoi8w4",
  "authDomain": "auth-lab-basem.firebaseapp.com",
  "projectId": "auth-lab-basem",
  "storageBucket": "auth-lab-basem.appspot.com",
  "messagingSenderId": "923039670065",
  "appId": "1:923039670065:web:f70c5cbe97fa47524a1a10",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


@app.route('/signin', methods = ['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    email = request.form['email']
    password = request.form['password']
    login_session['email'] = email
    login_session['password'] = password
    login_session['quote'] = []

    login_session['user'] = auth.sign_in_with_email_and_password(email, password)
    return redirect(url_for('home'))
    


@app.route('/home', methods = ['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
    quote = request.form['quote']
    login_session['quote'].append(quote)
    login_session.modified = True
    return redirect(url_for('display',quote=quote))

 




@app.route('/thanks', methods = ['GET', 'POST'])
def thanks():
  if request.method == 'GET':
    return render_template("thanks.html")
  else:
    return redirect(url_for('thanks'))






@app.route('/signout', methods = ['GET', 'POST'])
def signout():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    return redirect(url_for('signin'))
    auth.current_user = none


@app.route('/', methods = ['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      login_session['quote'] = []
      return redirect(url_for('signin'))
    except:
      error = "Authentication failed"
    print(auth.create_user_with_email_and_password(email, password))
    return redirect(url_for('signin'))



@app.route('/display', methods = ['GET', 'POST'])
def display():
  return render_template("display.html")




















if __name__ == '__main__':
    app.run(debug=True)
