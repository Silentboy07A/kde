from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML login page
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        return f"<h3>Welcome, {user}!</h3>"  # Simple response
    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(debug=True)
