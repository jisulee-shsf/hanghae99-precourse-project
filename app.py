# 1. 필요 모듈 import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
import os
import secrets
from datetime import timedelta

# 2. 애플리케이션 생성
app = Flask(__name__)

# 3. 애플리케이션 및 데이터베이스 설정
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(10000), nullable = False)

with app.app_context():
    db.create_all()

# 4-1. 홈 라우트 정의
@app.route("/")
def home():
    userData = {}
    userData['username'] = session.get("username", None)
    userData['email'] = session.get("email", None)
    return render_template("home.html", data = userData)

# 4-2. 회원가입 라우트 정의
@app.route("/signUp", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        username_received = request.form.get("username", type=str)
        email_received = request.form.get("email", type=str)
        password1_received = request.form.get("password1", type=str)
        password2_received = request.form.get("password2", type=str)

        if username_received == "" or email_received == "" or password1_received == "" or password2_received == "":
            flash("입력되지 않은 값이 있습니다.")
            return redirect(url_for("home"))
        
        cnt = Users.query.filter_by(email = email_received).count()
        
        if cnt > 0:
            flash("중복된 이메일 주소입니다.")
            return redirect(url_for("home"))
        
        if password1_received != password2_received:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for("home"))

        user = Users(username = username_received, email = email_received, password = password1_received)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("home.html")

# 4-3. 로그인 라우트 정의
@app.route("/signIn/", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        email_received = request.form.get("email", type=str)
        password_received = request.form.get("password", type=str)

        if email_received == "" or password_received == "":
            flash("입력되지 않은 값이 있습니다.")
            return redirect(url_for("home"))
        
        user = Users.query.filter_by(email = email_received).first()
        
        if user is None:
            flash("일치하는 회원 정보가 없습니다.")
            return redirect(url_for("home"))
        else:
            if user.password == password_received:
                session["username"] = user.email
                session["email"] = user.email
                session.permanent = True
                return redirect(url_for("home"))
            else:
                flash("비밀번호가 일치하지 않습니다.")
                return redirect(url_for("home"))
    else: 
        return render_template("home.html")

# 4-4. 로그아웃 라우트 정의
@app.route("/signOut")
def signOut():
    session.clear()
    return redirect(url_for("home"))

# 5. 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)