from flask import render_template
#from flask_login import login_user
#from werkzeug.security import generate_password_hash,check_password_hash
#from WarwickHackAThon2.databaseTemplate import user
#from flask_login import login_required,current_user
#from WarwickHackAThon2 import db
from WarwickHackAThon2 import app

'''@app.route('/')
def subscribe():
    return render_template("subscribe.html")'''

'''@app.route("/",methods=["POST"])
def subscribe_POST():
    emailAddress = request.form.get("email")
    password = request.form.get("password")

    User = user.query.filter_by(email=emailAddress).first()

    if User:
        return redirect(url_for('accessAuthorisation.subscribe'))
    
    new_user = user()
    new_user.emailAddress = emailAddress
    passwordArg = generate_password_hash(password,method="sha256")
    new_user.password = passwordArg 

    db.session.add(new_user)
    db.session.commit()

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login",methods=["GET"])
def login_POST():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    User = user.query.filter_by(email=email).first()

    if not User or not check_password_hash(User.password,password):
        return redirect(url_for('accessAuthorisation.login'))
    
    return redirect(url_for("index.profile"))'''

@app.route("/")
#@login_required
def profile():
    return render_template("index2.html")

'''email=current_user.emailAddress'''