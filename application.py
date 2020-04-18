import os

from model import *
from flask import Flask, session,render_template, request,redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
   raise RuntimeError("DATABASE_URL is not set")

app.config['SQLALCHEMY_DATABASE_URI'] =os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configure session to use filesystem      
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session=Session()
@app.route("/")
def index():
    return "project 1:TODO"
@app.route("/Register", methods = ['POST', 'GET'])
def cont():
    db.create_all()
    if request.method =='POST':
        udata=model(request.form['username'],request.form['mailID'],request.form['phone'],request.form['pwd'])
        userd=model.query.filter_by(mailID=request.form['mailID']).first()
        if userd is not None:
            var='Email already exists..please login!!'
            return render_template("index.html",var=var)
        db.session.add(udata)
        db.session.commit()
        print("Sucesssfully Registered")
        var1='Registration Successful'
        return render_template("index.html",var1=var1)
    else:
        return render_template("index.html")
 