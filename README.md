# Stroke Risk Prediction Web Application

This is a Flask-based web application that predicts a patient's risk of stroke based on clinical and lifestyle factors. It uses a trained Random Forest classifier and a minimalistic user interface.

---

## Features

- Predicts stroke probability using patient data  
- Powered by a trained Random Forest model  
- Color-coded risk bar visualization (green to red)   
- Mobile-friendly UI
---

##  Project Structure

```
stroke_application/
├── app.py                    # Flask app logic
├── random_forest_model.pkl   # Trained Random Forest model
├── scaler.pkl                # StandardScaler object
├── requirements.txt          # Required Python packages
├── render.yaml               # Render deployment config
│
├── static/
│   └── style.css             # App styling
│
└── templates/
    └── index.html            # Main HTML form
```

---

## Input Fields

| Field              | Type        | Description                          |
|-------------------|-------------|--------------------------------------|
| Age               | Numeric     | Patient's age (0–82)                 |
| BMI               | Numeric     | Body Mass Index (10–100)            |
| Average Glucose   | Numeric     | Blood glucose level (0–400)         |
| Hypertension      | Boolean     | 0 = No, 1 = Yes                      |
| Heart Disease     | Boolean     | 0 = No, 1 = Yes                      |
| Gender            | Categorical | Male / Female                        |
| Ever Married      | Categorical | Yes / No                             |
| Residence Type    | Categorical | Urban / Rural                        |
| Smoking Status    | Categorical | Never / Former / Smokes             |

---

## Model Details

The model was trained on a Kaggle stroke dataset with over 50,000 records. Features were cleaned, scaled, and one-hot encoded. Class imbalance was addressed during preprocessing.

**Best Performing Model:** Random Forest  
**Metrics:**

- Accuracy: 99%  
- F1 Score: 0.99  
- AUC Score: 0.9998  

For model training and evaluation, see the Stroke Prediction Model repo: [Cerebralstroke](https://github.com/BrandyRumRum/Stroke-Prediction-Model)

---

## Deployed Demo

Try out the live app here:  
[Deployed App](https://stroke-prediction-applicaiton.onrender.com)

---

## Authors

- Rajiv Ramcharan – 816034922  
- Brandon Ramcharitar – 816037181  
- Reuel Roberts – 816037539  
- Kylan Baksh – 816035777
