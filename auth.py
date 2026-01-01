from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint('auth', __name__)


mysql = None
bcrypt = None
#invalid_cred = "Invalid credentials"

def init_auth(app, mysql_instance, bcrypt_instance):
    global mysql, bcrypt
    mysql = mysql_instance
    bcrypt = bcrypt_instance
    app.register_blueprint(auth_bp)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(
            request.form['password']
        ).decode('utf-8')

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password FROM users WHERE username=%s",
            (username,)
        )
        data = cursor.fetchone()
        cursor.close()
        conn.close()

        if data and bcrypt.check_password_hash(data[0], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            
            return render_template('login.html', invalid_cred="Invalid credentials")

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))
