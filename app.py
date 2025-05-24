from flask import Flask, render_template, request, redirect, url_for, session
from Algo import calorieBurn

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session to store messages

predictor = calorieBurn()  # Create model object

@app.route("/", methods=['GET', 'POST'])
def calories_calc():
    if request.method == 'POST':
        try:
            gender = request.form.get('Gender')
            age = request.form.get('age')
            duration = request.form.get('Duration')
            heart_beat = request.form.get('heart_beat')
            temp = request.form.get('temp')
            bmi = request.form.get('BMI')

            # Handle empty input fields
            if '' in [gender, age, duration, heart_beat, temp, bmi]:
                session['message'] = "⚠️ Please fill in all fields."
                return redirect(url_for('calories_calc'))

            def encode_gender(g): return 0 if g == 'Male' else 1
            gender = encode_gender(gender)

            # Convert to float
            age = float(age)
            duration = float(duration)
            heart_beat = float(heart_beat)
            temp = float(temp)
            bmi = float(bmi)

            # Get prediction
            result = predictor.predict(gender, age, duration, heart_beat, temp, bmi)
            predicted_calories = max(0, round(result[0], 2))  # Ensure non-negative
            session['message'] = f"🔥 Predicted Calories Burned: {predicted_calories}"
        except Exception as e:
            session['message'] = f"❌ Error: {str(e)}"

        return redirect(url_for('calories_calc'))  # Redirect to clear POST data

    # GET request
    message = session.pop('message', None)
    return render_template('index.html', message=message)


