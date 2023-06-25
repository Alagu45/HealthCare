from flask import Flask, jsonify, request, render_template,redirect
from fhir.resources import patient
from fhir.resources import humanname
from fhir.resources import contactpoint
from fhir.resources import address
from fhir.resources import reference
from fhir.resources import observation
#from flask_login import LoginManager

#login_manager = LoginManager()
import mysql.connector


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#login_manager.init_app(app)

#@login_manager.user_loader
#def load_user(user_id):
#    return User.get(user_id)
# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '849730',
    'database': 'flaskapp',
}

# Connect to MySQL
db = mysql.connector.connect(**db_config)


# Endpoint for retrieving patient care records
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient_record(patient_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = %s", [patient_id])
    patient_data = cursor.fetchone()
    cursor.close()

    if patient_data:
        patient_obj = patient.Patient()
        patient_obj.id = patient_data[0]

        name_obj = humanname.HumanName()
        name_obj.text = patient_data[1]
        patient_obj.name = [name_obj]

        telecom_obj = contactpoint.ContactPoint()
        telecom_obj.system = 'email'
        telecom_obj.value = patient_data[2]
        patient_obj.telecom = [telecom_obj]

        patient_obj.gender = patient_data[3]
        patient_obj.birthDate = patient_data[4]

        address_obj = address.Address()
        address_obj.text = patient_data[5]
        patient_obj.address = [address_obj]

        observation_obj = observation.Observation()
        observation_obj.code = {'text': 'Medical History'}
        observation_obj.subject = reference.Reference({'reference': f'Patient/{patient_obj.id}'})
        observation_obj.valueString = patient_data[9]
        patient_obj.extension = [observation_obj]

        patient_json = patient_obj.as_json()

        return jsonify(patient_json)
    else:
        return jsonify({'error': 'Patient record not found'}), 404

# Endpoint for creating a new patient record
@app.route('/patient', methods=['GET','POST'])
def create_patient_record():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        dob = request.form['dob']
        address = request.form['address']
        phone = request.form['phone']
        bloodgroup = request.form['bloodgroup']
        height = request.form['height']
        weight = request.form['weight']
        medical_history = request.form['medicalhistory']
        allergies = request.form['allergies']
        medications = request.form['medications']
        emergency_contact = request.form['emergencycontact']
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO patients (name, email, gender, dob, address, phone, bloodgroup, height, weight, medicalhistory, allergies, medications, emergencycontact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, email, gender, dob, address, phone, bloodgroup, height, weight, medical_history, allergies, medications, emergency_contact))
            cursor.execute('select id from patients where email=%s',(email,))
            ids=cursor.fetchone()


            cursor.close()
            return render_template('successapi.html',id=ids[0])
        except:
            return render_template('healthapi.html',i='enter vailid date')
        db.commit()

    return render_template('healthapi.html')
    #return jsonify({'message': 'Patient record created'}), 201

@app.route("/")
def admin():
    return render_template('healthapi.html')
@app.route('/loged',methods=['GET'])
def loged():
    return render_template("adminsecond.html")
# Serve the index.html file
@app.route('/admin',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=db.cursor()
        cursor.execute('select * from ADMIN_NAME')
        fetched=cursor.fetchone()
        db  .commit()
        print(fetched)
        if username in fetched and password in fetched:
            return redirect('/loged')

        else:
            return render_template('admin.html', message='invalid user')

    return render_template('admin.html')

@app.route('/oldpatients')
def table():


    return render_template("adminsecond.html")
@app.route('/allpatients', methods=['GET','POST'])
def allpatient():
    cursor=db.cursor()
    cursor.execute('select * from patients')
    rows=cursor.fetchall()

    return render_template("allpatient.html",rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
