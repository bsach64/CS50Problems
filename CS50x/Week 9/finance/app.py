import os
import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        data = lookup(request.form.get("symbol"))
        if data != None:
            convert = usd(data["price"])
            return render_template("quoted.html", data=data, convert=convert)
        else:
            return apology("No such stock found")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]+$'
        confirmation = request.form.get("confirmation")
        if username == "":
            return apology("Username cannot be empty")
        elif password == "":
            return apology("Password cannot be empty")
        elif confirmation == "":
            return apology("Please reenter your password")
        elif password != confirmation:
            return apology("Password does not match")
        if re.match(pattern, password):
            ...
        else:
            return apology("Enter a valid password")
        existing = db.execute("SELECT username FROM users")
        for name in existing:
            if username  == name["username"]:
                return apology("Username already taken")
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]
    user_data = db.execute("SELECT symbol, share_count FROM owns WHERE user_id = ?", user_id)
    list_symbols = []
    for symbol in user_data:
        list_symbols.append(symbol["symbol"])
    if request.method == "POST":
        sell_symbol = request.form.get("symbol")
        if not sell_symbol in list_symbols:
            return apology("You Don't Own Such Stock")
        sell_share = request.form.get("shares")
        final_share = 0
        if int(sell_share) < 0:
            return apology("Number of shares should be positive")
        check = 1
        for entry in user_data:
            if entry["symbol"] == sell_symbol:
                check = 1
                stock_data = lookup(sell_symbol)
                user_data = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
                cash_add = float(stock_data["price"]) * int(sell_share)
                db.execute("UPDATE users SET cash = ? WHERE id = ?", (cash_add + float(user_data[0]["cash"])), user_id)
                if int(sell_share) > int(entry["share_count"]):
                    return apology("You don't own so many shares")
                else:
                    final_share = int(entry["share_count"]) - int(sell_share)
                db.execute("INSERT INTO transactions (user_id, symbol, stock_name, price, share_count, transaction_type, transaction_date) VALUES(?, ?, ?, ?, ?, 'sold', ?)", user_id, sell_symbol, stock_data["name"], float(stock_data["price"]), int(sell_share), datetime.now())
                db.execute("UPDATE owns SET share_count = ? WHERE user_id = ? AND symbol = ?", final_share, user_id, sell_symbol)
                return redirect("/")
            else:
                check = 0
        if check == 0:
            return apology("You don't Own such stock")
    return render_template("sell.html", list_symbols=list_symbols)