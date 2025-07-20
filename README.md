# 🥗 Calorie Expenditure Prediction Project

This project focuses on predicting **Calories Burned** based on biometric and activity data using multiple machine learning algorithms. The objective was to build regression models that accurately predict the calorie expenditure of individuals during physical activities.

---

## 📊 Project Overview

### Goal

To develop a machine learning pipeline capable of predicting calorie loss using input features like:

* Age
* Height
* Weight
* Duration of activity
* Heart Rate
* Body Temperature
* Gender

---

## 📝 Dataset Description

The project utilizes a tabular dataset with the following features:

* **id** — Unique identifier
* **Gender (Sex)** — Male/Female
* **Age** — Age in years
* **Height** — Height in centimeters
* **Weight** — Weight in kilograms
* **Duration** — Duration of activity in minutes
* **Heart\_Rate** — Average heart rate during activity
* **Body\_Temp** — Body temperature during activity
* **Calories** — Calories burned (target variable)

---

## ⚙️ Workflow Summary

### 1. Data Cleaning and Feature Engineering

* Added a **BMI** feature derived from height and weight.
* Encoded categorical variables using one-hot encoding (Sex).
* Removed irrelevant columns (e.g., `id`).

### 2. Exploratory Data Analysis (EDA)

* Visualized distributions of numerical features.
* Analyzed feature relationships with calories using:

  * Correlation heatmaps
  * Scatter plots
  * Pair plots
  * Box plots (for gender-based calorie differences)

### 3. Model Development

* **Linear Regression** — Simple baseline model.
* **XGBoost Regressor** — Tuned for performance using GridSearchCV.
* **Random Forest Regressor** — Evaluated as a strong ensemble model.

### 4. Model Evaluation

* Used **Root Mean Squared Logarithmic Error (RMSLE)** as the primary metric.
* Clipped negative predictions to zero since negative calorie loss is illogical.
* Visualized:

  * Actual vs Predicted scatter plots
  * Residual distribution plots
  * Feature importance (for XGBoost)

### 5. Hyperparameter Tuning

* Fine-tuned the XGBoost model using **GridSearchCV** with RMSLE as the scoring metric.
* Compared performance across models.

### 6. Model Persistence

* Final models saved using **pickle**:

  * `lr_model.pkl`
  * `xgb_model.pkl`
  * `forest_model.pkl`

### 7. Prediction Pipeline

* Created a **make\_predictions()** function for quick inference on unseen data (`test.csv`).

---

## 🏆 Model Performance Snapshot

| Model             | Validation RMSLE       |
| ----------------- | ---------------------- |
| Linear Regression | ✅ Baseline             |
| Random Forest     | ✅ Improved performance |
| XGBoost (Tuned)   | 🥇 Best Performance    |

---

## 📁 Project Structure

```
├── calorie_expenditure_prediction.py
├── make_predictions.py
├── train.csv
├── test.csv
├── lr_model.pkl
├── xgb_model.pkl
├── forest_model.pkl
└── README.md
```

---

## 🖊️ Future Improvements

* Deploy the model via a simple web app (e.g., Flask/Streamlit)
* Add cross-validation pipelines
* Integrate more advanced model ensembling techniques

---

## 📌 Key Takeaways

✅ Hands-on experience with feature engineering and model tuning
✅ Comparative analysis of regression algorithms
✅ Practical application of RMSLE in real-world scenarios

---

## 💡 Author

**Your Name**
Abdullateef Kawonise
(https://github.com/Kalab191)



