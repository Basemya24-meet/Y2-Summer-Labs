from flask import Flask,render_template,request,url_for,redirect
import random
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = "secret"




firebaseConfig = {
  "apiKey": "AIzaSyBIe03NljlABJK0ryB9TBj6B0bUOx2lzhw",
  "authDomain": "basem-s-y2-project.firebaseapp.com",
  "databaseURL": "https://basem-s-y2-project-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "basem-s-y2-project",
  "storageBucket": "basem-s-y2-project.appspot.com",
  "messagingSenderId": "773328288243",
  "appId": "1:773328288243:web:c068f53fe2f5fc2921fa86",
  "databaseURL":"https://basem-s-y2-project-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()

@app.route('/', methods = ['GET', 'POST'])
def main():
  return render_template("main.html")



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
    username = request.form ['username']
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      UID = login_session['user']['localId']
      user = {"username": username, "email": email}
      db.child("Users").child(UID).set(user)
      return redirect(url_for('choice'))
    except:
      return render_template("error_signup.html")


@app.route('/signin', methods = ['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)

      

      return redirect(url_for('choice'))
    except:
      return render_template("error_signin.html")


@app.route('/choice', methods = ['GET', 'POST'])
def choice():
  if request.method == 'GET':
    return render_template("choice.html")


@app.route('/search', methods = ['GET', 'POST'])
def search():
  if request.method == 'GET':
    # star=request.form['star']
    return render_template("search.html")
  else:
    return redirect(url_for('search'))


    # if answer == "1_star":
    #   user["discreption"] = discreption



@app.route('/add', methods = ['GET', 'POST'])
def add():
  if request.method == 'GET':
    return render_template("add.html")
  else:
    discreption = request.form['discreption']
    star = request.form['star']
    name_show = request.form['name_show']
    geners = request.form['geners']
    UID = login_session['user']['localId']

    info = {"name of the show": name_show,"gener": geners, "discreption:": discreption, "star": star, "UID": UID}

    db.child('reviews').push(info)
    return redirect(url_for('thanks', info = info))


@app.route('/thanks', methods = ['GET', 'POST'])
def thanks():
  if request.method=='POST':
    auth.current_user=None
    return redirect(url_for('signin'))
  return render_template("thanks.html")

@app.route('/display', methods = ['GET', 'POST'])
def display():
  reviews = db.child('reviews').get().val()

  return render_template("display.html", reviews = reviews)





if __name__ == '__main__':
    app.run(debug=True)