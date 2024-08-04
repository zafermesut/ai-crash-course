from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('salary.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    exp = request.form.get('experience')
    test = request.form.get('test')
    interview = request.form.get('interview')
    prediction = model.predict([[float(exp), float(test), float(interview)]])
    salary_prediction = float(prediction[0])

    return render_template('index.html', prediction_text=f'Employee Salary will be $ {salary_prediction:.2f}')


if __name__ == '__main__':
    app.run(debug=True)