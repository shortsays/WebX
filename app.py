from flask import Flask, render_template, request
import random

app = Flask(__name__)

doctors = {
    "allergist": ["Dr. Pawan", "Dr. Gupta"],
    "anesthesiologist": ["Dr. Ram", "Dr. Anjali"],
    "cardiologist": ["Dr. Pradeep", "Dr. Jain"],
    "dermatologist": ["Dr. Bhati", "Dr. Arti"],
    "endocrinologist": ["Dr. Shiv", "Dr. Amit"],
    "orthopedic": ["Dr. Rakhi", "Dr. Aditya"],
    "gynaecologist": ["Dr. Chandni", "Dr. Ankit"],
    "psychiatrist": ["Dr. Navin", "Dr. Ravi"],
    "radiologist": ["Dr. Sudhir", "Dr. Ajay"],
    "urologist": ["Dr. Wasim", "Dr. Singh"],
    "surgeon": ["Dr. Anurag", "Dr. Ashish"],
    "neurologist": ["Dr. Raj", "Dr. Mohit"],
    "oncologist": ["Dr. Rajesh", "Dr. Suresh"]
}
.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fullname = request.form.get('fullname', 'Anonymous')
        age = request.form.get('years', 'N/A')
        specialist = request.form.get('specialist')
        appointment_date = request.form.get('appointment_date')

        if not specialist or specialist not in doctors:
            return "Invalid specialist selection", 400
        
        assigned_doctor = random.choice(doctors[specialist])
        return render_template('result.html', fullname=fullname, age=age, doctor=assigned_doctor,appointment_date=appointment_date)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)