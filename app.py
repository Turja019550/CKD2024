from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest model
model = pickle.load(open('rd_clf_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        serum_creatinine = float(request.form['serum_creatinine'])
        blood_urea = float(request.form['blood_urea'])
        blood_pressure = float(request.form['blood_pressure'])
        albumin = float(request.form['albumin'])
        haemoglobin = float(request.form['haemoglobin'])

        # Create an array with the inputs
        input_features = np.array([[serum_creatinine, blood_urea, blood_pressure, albumin, haemoglobin]])

        # Make the prediction using the loaded model
        prediction = model.predict(input_features)

        # Map the prediction to the corresponding class
        if prediction == 0:
            result = 'This Patient is Diagnosed with CKD'
        else:
            result = 'Not Diagnosed with CKD'

        return render_template('index.html', prediction_text=f'Predicted Class: {result}')

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
