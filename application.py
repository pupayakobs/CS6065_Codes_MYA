from flask import Flask, request, redirect, url_for, render_template_string, send_file
import sqlite3
import io

app = Flask(__name__)
app.secret_key = 'change-this-to-any-random-string'

DB_PATH = '/var/www/flaskapp/CS6065MYA.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

REGISTER_FORM = """
<h1>Register</h1>
<form method="POST" enctype="multipart/form-data">
  Username: <input type="text" name="username" required><br><br>
  Password: <input type="password" name="password" required><br><br>
  First Name: <input type="text" name="firstname" required><br><br>
  Last Name: <input type="text" name="lastname" required><br><br>
  Email: <input type="email" name="email" required><br><br>
  Address: <input type="text" name="address" required><br><br>
  Upload File: <input type="file" name="userfile" required><br><br>
  <input type="submit" value="Register">
</form>
<p><a href="/login">Already registered? Log in here</a></p>
"""

DISPLAY_TEMPLATE = """
<h1>Welcome, {{ firstname }} {{ lastname }}</h1>
<p>Email: {{ email }}</p>
<p>Address: {{ address }}</p>
<p>Uploaded file: {{ filename }}</p>
<p>Word count: {{ wordcount }}</p>
<a href="/download/{{ username }}"><button>Download File</button></a><br><br>
<a href="/login">Go to login page</a>
"""

LOGIN_FORM = """
<h1>Login</h1>
<form method="POST">
  Username: <input type="text" name="username" required><br><br>
  Password: <input type="password" name="password" required><br><br>
  <input type="submit" value="Login">
</form>
<p><a href="/">New user? Register here</a></p>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        address = request.form["address"]
        file = request.files["userfile"]
        filename = file.filename
        filedata = file.read()
        wordcount = len(filedata.decode("utf-8", errors="ignore").split())

        conn = get_db()
        conn.execute(
            "INSERT INTO users (username, password, firstname, lastname, email, address, filename, filedata, wordcount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (username, password, firstname, lastname, email, address, filename, filedata, wordcount)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("display", username=username))

    return render_template_string(REGISTER_FORM)

@app.route("/display/<username>")
def display(username):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    if user is None:
        return "User not found", 404
    return render_template_string(DISPLAY_TEMPLATE,
        firstname=user["firstname"], lastname=user["lastname"],
        email=user["email"], address=user["address"],
        filename=user["filename"], wordcount=user["wordcount"],
        username=user["username"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        conn.close()
        if user is None:
            return "Invalid username or password. <a href='/login'>Try again</a>"
        return redirect(url_for("display", username=username))
    return render_template_string(LOGIN_FORM)

@app.route("/download/<username>")
def download(username):
    conn = get_db()
    user = conn.execute("SELECT filename, filedata FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    if user is None:
        return "User not found", 404
    return send_file(io.BytesIO(user["filedata"]), download_name=user["filename"], as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
