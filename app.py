from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            avg_glucose = float(request.form['avg_glucose_level'])
            bmi = float(request.form['bmi'])
            gender = 1 if request.form['gender'] == 'Male' else 0
            married = 1 if request.form['ever_married'] == 'Yes' else 0

            numeric_scaled = scaler.transform([[age, avg_glucose, bmi]])[0]

            work_type_vector = [0, 0, 1, 0, 0]   # work_type_Private
            residence_vector = [1]              # Residence_type_Urban
            smoking_vector = [0, 0, 1, 0]        # smoking_status_never smoked

            input_data = np.array([
                numeric_scaled[0],       # age
                hypertension,
                heart_disease,
                numeric_scaled[1],       # glucose
                numeric_scaled[2],       # bmi
                gender,
                married,
                0, 0, 1, 0, 0,           # work_type_Private
                1,                       # Residence_type_Urban
                0, 0, 1                  # smoking_status_never smoked
            ]).reshape(1, -1)

            prob = model.predict_proba(input_data)[0][1]
            percent = int(prob * 100)

            if prob >= 0.6:
                label = "⚠️ <strong>High Stroke Risk</strong>"
                color = "#ff4c4c"
            elif prob >= 0.3:
                label = "🟠 <strong>Moderate Risk</strong>"
                color = "#ffa500"
            elif prob >= 0.15:
                label = "🟡 <strong>Mild Risk</strong>"
                color = "#ffff66"
            else:
                label = "🟢 <strong>Low Risk</strong>"
                color = "#66ff66"

            result = f"""
                <div style='text-align:center;'>
                    <div style='margin-bottom:10px;color:{color};'>
                        {label}<br>Probability: {prob:.2f}
                    </div>
                    <div class='result-bar'>
                        <div class='result-bar-fill' style='width:{percent}%; background-color:{color};'></div>
                    </div>
                </div>
            """

            return render_template('index.html', result=result)

        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")

    return render_template('index.html', result=None)

if __name__ == '__main__':
    import webbrowser, threading
    threading.Timer(1.0, lambda: webbrowser.open_new('http://127.0.0.1:5000/')).start()
    app.run(debug=True)
