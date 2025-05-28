
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'

# Hardcoded user and admin credentials
USERS = {
    'user': 'user123',
    'admin': 'admin123'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == USERS.get('admin'):
            session['username'] = username
            return redirect(url_for('admin_home'))
        elif username == 'user' and password == USERS.get('user'):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session and session['username'] == 'user':
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/admin')
def admin_home():
    if 'username' in session and session['username'] == 'admin':
        return render_template('admin.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

