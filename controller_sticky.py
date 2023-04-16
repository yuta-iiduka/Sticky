from flask import (
    Flask,
    url_for, flash, request,
    render_template, redirect
)

from flask_login import (
    LoginManager, UserMixin,
    login_required,
    current_user,
    login_user, logout_user
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "f4Pjp3UgJa51"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sticky.db"

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    stickies = Sticky.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html",stickies=stickies)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            user = User(
                username=username,
                password=password,
                email=""
            )
            db.session.add(user)
            db.session.commit()
            user = User.query.filter_by(username=username,password=password).first()
            sticky = Sticky(
                user_id = user.id
                ,sticky_id = str(user.id) + "_" + str(0)
                ,title = "サンプル"
                ,content = "ここに内容を入力します。"
            )
            db.session.add(sticky)
            db.session.commit()
        login_user(user)
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route('/sticky/<sticky_id>', methods=['POST'])
@login_required
def sticky_update(sticky_id):
    sticky = Sticky.query.filter_by(sticky_id=sticky_id).first()
    data = json.loads(request.get_data())
    print(data)
    if sticky is None:
        sticky = Sticky(
                user_id   = current_user.id,
                sticky_id = sticky_id,
                content   = data["content"],
                title     = data["title"],
                color     = data["color"],
                top       = int(data["top"]),
                left      = int(data["left"]),
                height    = int(data["height"]),
                width     = int(data["width"])
        )
    else:
        sticky.content = data["content"]
        sticky.title   = data["title"]
        sticky.color   = data["color"]
        sticky.top     = int(data["top"])
        sticky.left    = int(data["left"])
        sticky.height  = int(data["height"])
        sticky.width   = int(data["width"])
    db.session.add(sticky)
    db.session.commit()
    
    return "登録しました"

@app.route('/sticky/delete/<sticky_id>', methods=['POST'])
@login_required
def sticky_delete(sticky_id):
    sticky = Sticky.query.filter_by(sticky_id=sticky_id).delete()
    db.session.commit()
    
    return "削除しました"


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email    = db.Column(db.String, default="")


class Sticky(db.Model):
    __tablename__ = "sticky"
    id        = db.Column(db.Integer, primary_key=True)
    user_id   = db.Column(db.Integer, nullable=False)
    sticky_id = db.Column(db.String,  default="")
    title     = db.Column(db.String,  default="")
    content   = db.Column(db.String,  default="")
    status    = db.Column(db.Integer, default=0)
    top       = db.Column(db.Integer, default=5)
    left      = db.Column(db.Integer, default=5)
    height    = db.Column(db.Integer, default=10)
    width     = db.Column(db.Integer, default=10)
    color     = db.Column(db.String , default="grey")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="55555", threaded=True)
