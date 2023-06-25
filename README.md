# HealthCare
The application provides functionality for managing patient records and allows users to retrieve patient information and create new patient records.

# Description:

## Flask Application:
   The project initializes a Flask application using the `Flask` class from the `flask` module. It creates an instance of the Flask app and sets some configuration options.

## MySQL Database Connection:
   The application establishes a connection to a MySQL database using the `mysql.connector` module. It specifies the database configuration details such as the host, username, password, and database name.

## Route for Retrieving Patient Records:
   The application defines an endpoint (`/patients/<patient_id>`) that handles GET requests for retrieving patient records. It accepts a patient ID as a parameter and queries the database to fetch the corresponding patient record. The retrieved data is then transformed into a FHIR-compliant JSON representation using the `fhir.resources` module and returned as a response.

## Route for Creating a New Patient Record:
   The application defines an endpoint (`/patient`) that handles both GET and POST requests for creating a new patient record. In the case of a POST request, the endpoint retrieves the form data submitted by the user (name, email, gender, dob, address, etc.), inserts the data into the MySQL database, and returns a success message or error message as a response.


## User Interface:
   The application uses Flask's `render_template` function to serve HTML templates. It provides user interfaces for various pages, including the main health API form (`/`), the admin login page (`/admin`), an admin dashboard (`/loged`), and a page to display all patients' records (`/allpatients`)
user instructions for this healthcare application:


## Accessing the Application:
   - Open a web browser and enter the URL where the application is hosted.
   - The main page will be displayed, showing a form to create a new patient record.


## Creating a New Patient Record:
   - Fill in the required information in the form, such as name, email, gender, date of birth, address, phone number, blood group, height, weight, medical history, allergies, medications, and emergency contact.
   - Click the "Submit" or "Create" button to create the patient record.
   - If the record is successfully created, a success message will be displayed along with the assigned patient ID.
   - If there are any errors or invalid data, an error message will be shown, and you will need to correct the information and resubmit the form.


## Retrieving Patient Records:
   - To retrieve a patient's care record, you need to know the patient's ID.
   - In the URL of the application, append `/patients/<patient_id>`, replacing `<patient_id>` with the actual ID of the patient you want to retrieve.
   - The patient's record will be displayed as a JSON response, showing details such as name, email, gender, date of birth, address, and medical history.
   - If the patient record is not found, an error message will be displayed.


##  Admin Login (Restricted Access):
   - Access the admin login page by clicking on the "Admin Login" link or navigating to `/admin`.
   - Enter the admin username and password in the provided fields.
   - If the credentials are correct, you will be redirected to the admin dashboard (`/loged`).
   - If the credentials are incorrect, an error message will be displayed, and you can retry entering the correct credentials.

 
## Admin Dashboard:
   - Once logged in as an admin, you will have access to the admin dashboard.
   - From the dashboard, you can navigate to various sections, such as viewing all patient records (`/allpatients`).
   - Click on the respective links or buttons to access the desired sections.
## Viewing All Patient Records:
   - On the admin dashboard or by navigating to `/allpatients`, you can view all patient records stored in the database.
   - The records will be displayed in a tabular format, showing details such as the patient's ID, name, email, gender, date of birth, address, and other information.

Remember to ensure that the application is properly set up and running with the required dependencies, such as Flask, the MySQL database, and any other necessary components. Additionally, make sure to handle the security aspects of the application, such as securing admin access and protecting sensitive patient information.



