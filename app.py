from functools import wraps
import os
from pathlib import Path
from flask import Flask, render_template, redirect, url_for, flash
from flask_session import Session
from sql import SQL
from werkzeug.security import generate_password_hash

from controllers.user_controller import UserController
from models.user import User

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "database.db"

app = Flask(__name__)

app.secret_key = "your-secret-key-here" # IMPORTANT: change this to a random secret key !

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = str(BASE_DIR / "flask_session")
Session(app)

# create the sqlite database if the file does not exist
if not DATABASE_PATH.exists():
    DATABASE_PATH.open("w").close()

    # create the tables
    db = SQL(f"sqlite:///{DATABASE_PATH.as_posix()}")
    with (BASE_DIR / "database.sql").open("r", encoding="utf-8") as sql_file:
        for statement in sql_file.read().split(";"):
            if statement.strip():
                db.execute(statement)

    # insert an admin user
    admin_user = User("admin", generate_password_hash("adminpassword"))
    admin_id = db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", admin_user.login, admin_user.password_hash)
    print(f"Created admin user with ID {admin_id}: {admin_user}")
else:
    db = SQL(f"sqlite:///{DATABASE_PATH.as_posix()}")

@app.teardown_appcontext
def close_database(exception):
    db._disconnect()


user_controller = UserController(db)

def login_required(f):
    """
    Decorator to require login
    Redirects to the login page if the user is not logged in
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = None
        if True:  # TODO: check if the user is logged in
            flash("Please login first", "error")
            return redirect(url_for("login"))

        return f(user, *args, **kwargs)

    return decorated_function


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Hint: use the user_controller to check if the user exists
    return render_template("not_implemented.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("not_implemented.html")


@app.route("/user/<int:user_id>")
@login_required
def user_profile(user, user_id):  # 'user' is the current logged-in user from @login_required
    return "Not implemented yet", 501


if __name__ == "__main__":
    app.run(debug=True)
