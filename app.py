from flask import Flask, request, render_template

app = Flask(__name__)

# Home page - the form
@app.route('/')
def home():
    return render_template('index.html')

# When they submit the form
@app.route('/generate', methods=['POST'])
def generate_plan():
    # Get what the runner typed
    name = request.form['name']
    weeks = int(request.form['weeks'])
    days_per_week = int(request.form['days'])
    level = request.form['level']  # beginner, intermediate, advanced

    # Super simple logic (we’ll make it smarter later)
    if level == "beginner":
        base_miles = 10
    elif level == "intermediate":
        base_miles = 20
    else:
        base_miles = 35

    # Make a very dumb plan: just increase mileage a little every week
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
