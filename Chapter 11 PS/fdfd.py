from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded login credentials
USERNAME = 'admin'
PASSWORD = 'admin123'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return f"<h2>Welcome, {username}!</h2><p>You have successfully logged in.</p>"
        else:
            error = 'Invalid Username or Password'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
