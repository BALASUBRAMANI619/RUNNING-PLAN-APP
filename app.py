from flask import Flask, request, render_template
from auth import init_auth
from util import login_required
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()  # 👈 this loads .env for VS Code / local runs

# Secret key (use env var in real Docker setup)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")

# MySQL config (env vars recommended later)
app.config['MYSQL_DATABASE_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DATABASE_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DATABASE_DB'] = os.getenv("MYSQL_DB")
#print("MYSQL_HOST =", os.getenv("MYSQL_HOST"))

mysql = MySQL(app)
bcrypt = Bcrypt(app)

# Initialize auth blueprint
init_auth(app, mysql, bcrypt)

# 🔐 Home page (NOW PROTECTED)
@app.route('/')
@login_required
def home():
    return render_template('index.html')

# Generate plan (already protected)
@app.route('/generate', methods=['POST'])
@login_required
def generate_plan():
    name = request.form['name']
    weeks = int(request.form['weeks'])
    days_per_week = int(request.form['days'])
    level = request.form['level']

    if level == "beginner":
        base_miles = 10
    elif level == "intermediate":
        base_miles = 20
    else:
        base_miles = 35

    plan = []
    for week in range(1, weeks + 1):
        mileage_this_week = base_miles + (week - 1) * 2
        miles_per_run = round(mileage_this_week / days_per_week, 1)
        plan.append({
            "week": week,
            "total_miles": mileage_this_week,
            "per_run": miles_per_run,
            "days": days_per_week
        })

    return render_template('plan.html', name=name, plan=plan)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
