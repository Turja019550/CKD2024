TITLE:
Chronic Kidney Disease (CKD) Detection using Machine Learning

**Description**

🧠 Predicts Chronic Kidney Disease using machine learning.

📊 Trained on a dataset with 401 patient records and 26 medical features.

🤖 Used 10 ML algorithms; Random Forest achieved ~97% accuracy.

✅ Evaluated using accuracy, precision, recall, and F1-score.

🌐 Developed a Flask web app for real-time prediction.

🔬 Web app uses top 5 key features for input (e.g., Albumin
 , Serum Creatinine, Hemoglobin ,Blood Pressure, Blood Urea).
 
💾 Built with Python, scikit-learn, Flask, and Render.


**Dataset Summary**

📦 Samples: 401 patient records

⚖️ Balanced Data: Oversampling was applied to balance CKD and non-CKD cases

🧬 Features: 26 medical attributes (e.g., blood pressure, albumin, serum creatinine, hemoglobin, etc.)

**Machine Learning Algorithms Used**

Logistic Regression

Naive Bayes

Support Vector Machine (SVM)

K-Nearest Neighbors (KNN)

Decision Tree

Random Forest 🌟 (Best Performer)

XGBoost

LightGBM

CatBoost

AdaBoost

**Best Model: Random Forest**

✅ Accuracy: ~96%

✅ Precision, Recall, F1-Score: Higher than other models

✅ Selected for deployment in the web app

**Features Used in Web App**

Due to medical significance and model importance, only top 5 features were used for real-time prediction:

Albumin

Serum Creatinine

Hemoglobin

Blood Pressure

Blood Urea

**Web Application**

A Flask-based web app was developed to allow users to:

Enter patient values

Predict CKD or non-CKD in real time

View a simple result interface

🚀 Hosted on Render (or your hosting platform)

**Technologies Used**

Tool / Library	Purpose
Python	Programming language
Pandas, NumPy	Data processing
Scikit-learn	ML models
Matplotlib, Seaborn	Visualization
Flask	Web framework
PyCaret / XGBoost / LightGBM	Advanced models

**Visualizations**

Feature Importance (Random Forest)

Correlation Heatmap

SHAP & LIME Explainability (optional)







