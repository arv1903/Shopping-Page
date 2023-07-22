from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
app.permanent_session_lifetime = timedelta(hours=4)
Session(app)

@app.route("/index", methods=["GET", "POST"])
def index():
	if "username" in session:
		return redirect(url_for('user', username=session['username']))
	return render_template("index.html")

@app.route("/<username>")
def user(username):
	if "username" in session:
		return render_template("index.html")
	return redirect(url_for("login"))

@app.route("/about")
def about():

	return render_template("about.html")

@app.route("/contact")
def contact():

	return render_template("contact.html")

@app.route("/products")
def products():

	return render_template("products.html")

@app.route("/search")
def search():
	query = request.args.get("query")
	return redirect("https://www.google.com/search?q=" + query)

@app.route("/", methods=["GET", "POST"])
def login():
	if "username" in session:
		return redirect(url_for('index'))

	if request.method == "POST":
		username = request.form["username"] #request.form.get("username")
		password = request.form["password"] #request.form.get("password")
		if username == "jono" and password == "jonogantengbanget123":
			session["username"] = username
			return redirect(url_for('index'))

	return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop("username", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run()