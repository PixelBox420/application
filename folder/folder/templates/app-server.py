import time
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import subprocess
from werkzeug.utils import secure_filename
import os
import requests
import queue
from flask_sqlalchemy import SQLAlchemy
import threading

##languageTransfVaria = '2'
##doeshehaveaccountTransfVaria = '0'
#tryreplaceonnewsumbis maybefineifast transf
# Add a global variable to store the processing status
queue_length=0
#processing_complete = False
processing_result = None

#trycountotalappvisits
template_visit_count = 0

# Add a global variable to store the processing status and response data
processing_status = {"status": "pending", "data": {}}

# Add a global variable to store the processing status and response data
processing_status = {"status": "pending", "data": {}}
processing_lock = threading.Lock()

app = Flask(__name__)
user_queue = queue.Queue()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/try.db'  # SQLite database file path
db = SQLAlchemy(app)

class VisitCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False, default=0)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailx = db.Column(db.String(120), unique=True, nullable=False)
    passwordx = db.Column(db.String(120), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

# Create the necessary tables before running the app
create_tables()

def process_user_request(data, files):
    try:
        # Your existing processing logic here
        # This is where you handle the user data, interact with external services, etc.
        # ...
        server2_url = 'http://[REDACTED]:5000/run_app'
        response = requests.post(server2_url, data=data, files=files)
        # Check if the response content is JSON
        try:
            json_response = response.json()
            print("Server 2 response:", json_response)
            return json_response, response.status_code

        except ValueError:
            print("Server 2 response is not JSON")
            return None, response.status_code

    except Exception as e:
        return f"Error: {str(e)}", 500

# Add this configuration to allow larger file uploads
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

@app.route('/response_template', methods=['POST', 'GET'])
def response_template():
    global queue_length
    global template_visit_count
    # Your existing logic to retrieve form data
    #firstname = request.form.get('firstname')
    # ... (all other form fields)

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    # Additional logic to retrieve image paths
    ###
    template_visit_count = template_visit_count + 1
    image_path1 = 'static/tryeth.jpg'
    image_path2 = 'static/trybtc.jpg'

    # Additional logic for other variables
    language_of_service = request.form.get('languageOfService')
    accountOfService = request.form.get('accountOfService')
    completeness = 'yes'
    quelength = queue_length  # Assuming user_queue is defined
    
    # Render the template with all the variables
    return render_template('response_template.html',
                           image_path1=image_path1,
                           image_path2=image_path2,
                           language=language_of_service,
                           doeshehaveaccount=accountOfService,
                           completion='yes',
                           quelength=queue_length)


@app.route('/response_templatedeque', methods=['POST', 'GET'])
def response_templatedeque():
    global queue_length
    global template_visit_count
    # Your existing logic to retrieve form data
    #firstname = request.form.get('firstname')
    # ... (all other form fields)
    if queue_length >0:
        queue_length = queue_length -1

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    # Additional logic to retrieve image paths
    ###
    template_visit_count = template_visit_count + 1
    image_path1 = 'static/tryeth.jpg'
    image_path2 = 'static/trybtc.jpg'

    # Additional logic for other variables
    language_of_service = request.form.get('languageOfService')
    accountOfService = request.form.get('accountOfService')
    completeness = 'yes'
    quelength = queue_length  # Assuming user_queue is defined
    
    # Render the template with all the variables
    return render_template('response_template.html',
                           image_path1=image_path1,
                           image_path2=image_path2,
                           language=language_of_service,
                           doeshehaveaccount=accountOfService,
                           completion='yes',
                           quelength=queue_length)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    ##global template_visit_count
    ##template_visit_count = template_visit_count + 1
    global queue_length
    # Retrieve or create the VisitCount record
    ##visit_count_record = VisitCount.query.first()
    ##if not visit_count_record:
    ##    visit_count_record = VisitCount()
    ##    db.session.add(visit_count_record)

    ##visit_count_record.count += 1
    ##db.session.commit()
    ###
    emailx = request.form.get('emailx')
    passwordx = request.form.get('passwordx')
    # Additional logic to retrieve image paths
    image_path1 = 'static/tryeth.jpg'
    image_path2 = 'static/trybtc.jpg'

    # Additional logic for other variables
    language_of_service = request.form.get('languageOfService')
    accountOfService = request.form.get('accountOfService')
    completeness = 'yes'
    quelength = queue_length  # Assuming user_queue is defined
    # Access values submitted in the form
    trylanguage_of_servicexxx = request.form.get('trylanguagexxx')
    tryaccountOfServicexxx = request.form.get('trydoeshehaveaccountxxx')
    trycompletenessxxx = request.form.get('trycompletionxxx')
    tryquelengthxxx = request.form.get('tryquelengthxxx')
    # tryseeifexistandtryprovidetempatewithweirdsvaluetonotif
    print(trylanguage_of_servicexxx)
    print(tryaccountOfServicexxx)
    print(trycompletenessxxx)
    print(tryquelengthxxx)
    # Check if the email or password already exists in the database
    existing_user = User.query.filter_by(emailx=emailx).first()
    if existing_user:
        # Render the template with all the variables
        return redirect(url_for('response_template', quelength=tryquelengthxxx, language=trylanguage_of_servicexxx, completion='yes', doeshehaveaccount=tryaccountOfServicexxx, trypro='alrdextsr'))
        return render_template('response_template.html',
                           image_path1=image_path1,
                           image_path2=image_path2,
                           language=trylanguage_of_servicexxx,
                           doeshehaveaccount=tryaccountOfServicexxx,
                           completion=trycompletenessxxx,
                           quelength=tryquelengthxxx, trypro='alrdextsr')
    # Store the user information securely (e.g., in a database)

    # Store the user information in the SQLite database
    new_user = User(emailx=emailx, passwordx=passwordx)
    db.session.add(new_user)
    db.session.commit()
    
    # For demonstration purposes, print the user information
    print(f"Email: {emailx}, Password: {passwordx}")
    # Your existing logic to retrieve form data
    #firstname = request.form.get('firstname')
    # ... (all other form fields)


    # Render the template with all the variables
    return redirect(url_for('response_template', quelength=tryquelengthxxx, language=trylanguage_of_servicexxx, completion='yes', doeshehaveaccount=tryaccountOfServicexxx, trypro='pro'))
    return render_template('response_template.html',
                           image_path1=image_path1,
                           image_path2=image_path2,
                           language=trylanguage_of_servicexxx,
                           doeshehaveaccount=tryaccountOfServicexxx,
                           completion='yes',
                           quelength=tryquelengthxxx, trypro='pro')

##def send_welcome_email(email):
##    try:
##        msg = Message('Welcome to Your App', sender='your_email@example.com', recipients=[email])
##        msg.body = 'Thank you for signing up! Welcome to Your App.'
##        mail.send(msg)
##        print("Email sent successfully.")
##    except Exception as e:
##        print(f"Error sending email: {str(e)}")

@app.route('/another_page')
def another_page():
    global template_visit_count
    template_visit_count = template_visit_count + 1

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    ###
    section = request.args.get('section')
    language = request.args.get('language', 'en')  # Default to 'en' if not provided

    # Your logic to render the page based on the section and language
    return render_template('another_page.html', language=language)

@app.route('/another_page/<section>')
def another_page_seq(section):
    ##global template_visit_count
    ## = template_visit_count + 1

    section = request.args.get('section')
    language = request.args.get('language', 'en')  # Default to 'en' if not provided

    # Your logic to render the page based on the section and language
    return render_template('another_page.html', language=language)

# Additional route for the "Privacy" section
@app.route('/privacy')
def privacy():
    global template_visit_count
    template_visit_count = template_visit_count + 1
    
    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    ###

    return render_template('another_page.html', section='#privacy')


# Add a route to render the response_template for testing
@app.route('/test_response')
def test_response():
    global template_visit_count
    template_visit_count = template_visit_count + 1

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    ###
    # Assuming the image paths are available
    image_path1 = "static/trybtc.jpg"
    image_path2 = "static/tryeth.jpg"
    # Use request.args for GET requests
    language = request.args.get('language', 'en')  # Default to 'en' if not provided
    account_of_service = request.args.get('accountOfService')
    # Get the language from the session
    ####language = session.get('language', 'en')  # Default to English if language is not set
    # Render the response_template with image paths
    return render_template('response_template.html', image_path1=image_path1, image_path2=image_path2, language=language, doeshehaveaccount=account_of_service)

# Add a route to render the response_template for testing
@app.route('/loading')
def loading():
    global template_visit_count
    template_visit_count = template_visit_count + 1

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    ###
    # Assuming the image paths are available
    image_path1 = "static/trybtc.jpg"
    image_path2 = "static/tryeth.jpg"
    
    # Use request.args for GET requests
    language = request.args.get('language', 'en')  # Default to 'en' if not provided
    account_of_service = request.args.get('accountOfService')
    # Get the language from the session
    ####language = session.get('language', 'en')  # Default to English if language is not set
    
    # Render the response_template with image paths
    return render_template('loading.html', image_path1=image_path1, image_path2=image_path2, language=language, doeshehaveaccount=account_of_service)



@app.route('/run_app', methods=['POST'])
def run_app():
    global queue_length
    #global processing_complete
    #global processing_status
    global user_queue
    global template_visit_count
    #with processing_lock:
       # queue_length = user_queue.qsize()
    if request.method == 'POST':
        try:
            ##template_visit_count = template_visit_count + 1
            queue_length = queue_length + 1
            
            # Retrieve or create the VisitCount record
            ##visit_count_record = VisitCount.query.first()
            ##if not visit_count_record:
            ##    visit_count_record = VisitCount()
            ##    db.session.add(visit_count_record)

            ##visit_count_record.count += 1
            ##db.session.commit()
            ###
            #file_path = ''  # Initialize file_path with a default value 
            #file_pathx = ''  # Initialize file_path with a default value 
            #file_pathxxxx = ''  # Initialiefault value 
            # Initialize file paths
            file_path = ''
            file_pathx = ''
            file_pathxxxx = ''

            file = request.files.get('fileInput')
            filex = request.files.get('fileInputx')
            filexxxx = request.files.get('fileInputxxxx')
            print(filex)

            # Check if files are present in the request for 'fileInput'
            if file and file.filename != '':
                print('asc')
                file = request.files['fileInput']
                filename = secure_filename(file.filename)
                file_path = os.path.join("uploads", filename)
                file.save(file_path)
                # Get the absolute path to the saved file
                file_path = os.path.abspath(os.path.join('uploads', filename))
            else:
                file_path = ''

              # Check if files are present in the request for 'fileInputx'
            if filex and filex.filename != '':
                filex = request.files['fileInputx']
                filenamex = secure_filename(filex.filename)
                file_pathx = os.path.join("uploads", filenamex)
                filex.save(file_pathx)
                # Get the absolute path to the saved file
                file_pathx = os.path.abspath(os.path.join('uploads', filenamex))
            else:
                file_pathx = ''

                # Check if files are present in the request for 'fileInputxxxx'
            if filexxxx and filexxxx.filename != '':
                filexxxx = request.files['fileInputxxxx']
                filenamexxxx = secure_filename(filexxxx.filename)
                file_pathxxxx = os.path.join("uploads", filenamexxxx)
                filexxxx.save(file_pathxxxx)
                # Get the absolute path to the saved file
                file_pathxxxx = os.path.abspath(os.path.join('uploads', filenamexxxx))
            else:
                file_pathxxxx = ''
                # Pass the file path to the Selenium script
                #selenium_data = {
                #    'firstname': firstname,
                #    'lastname': lastname,
                #    # ... other form data ...
                #    'file_path': file_path
                #}
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            henkilotunnus = request.form.get('henkilotunnus')
            address = request.form.get('address')
            postnumber = request.form.get('postnumber')
            city = request.form.get('city')
            phone = request.form.get('phone')
            email = request.form.get('email')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            nationality = request.form.get('nationality')  # Add this line to retrieve the nationality value
            education_level = request.form.get('educationLevel')
            language_of_service = request.form.get('languageOfService')
            school_id = request.form.get('schoolId')
            gender = request.form.get('gender')
            moveToCapitalArea = request.form.get('moveToCapitalArea')
            tulolaji = request.form.get('tulolaji')
            monthly_income = request.form.get('monthly_income')
            Varallisuutta = request.form.get('Varallisuutta')
            Varallisuusmaara = request.form.get('Varallisuusmaara')
            lisatiedot = request.form.get('lisatiedot')
            student_number = request.form.get('student_number')
            housingSituationSelect = request.form.get('housingSituationSelect')
            applicationReasonSelect = request.form.get('applicationReasonSelect')
            accountOfService = request.form.get('accountOfService')
            Loginemail = request.form.get('Loginemail')
            Loginpassword = request.form.get('Loginpassword')
            hometype = request.form.get('hometype')
            area =  request.form.get('area')
            input_birth_date  =  request.form.get('input_birth_date')
            languageOfServicePass = request.form.get('languageOfServicePass')
            applicationReasonHoaSelect = request.form.get('applicationReasonHoaSelect')
            completeness = request.form.get('completeness')
            Makepassword = request.form.get('Makepassword')
            stateID = request.form.get('stateID')
            desired_rent = request.form.get('desired_rent')

            #file_path = file_path.replace("elias", "johns")
            # Now use modified_path in your code
            #file_pathx = file_pathx.replace("elias", "johns")
            # Now use modified_path in your code
            #file_pathxxxx = file_pathxxxx.replace("elias", "johns")
            # Now use modified_path in your code

            print('Received firstname from index.html:', firstname)
            print('Received firstname from index.html:', lastname)
            print(file_path)
            print(lisatiedot)
            print(gender)
            print("Accountofservice:",accountOfService);
            print("birthdate", input_birth_date)
            print("AccountofservicePass:",languageOfServicePass);
            print("language", languageOfServicePass)
            # Check if any of the required fields is None
            if firstname is None or lastname is None or henkilotunnus is None:
                return "Missing required fields", 400

            
            # Prepare data to send to the Windows laptop
            data = {
                'firstname': firstname,
                'lastname': lastname,
                'henkilotunnus': henkilotunnus,
                'address': address,
                'postnumber': postnumber,
                'city': city,
                'phone': phone,
                'email': email,
                'start_date': start_date,
                'end_date': end_date,
                'nationality': nationality,
                'education_level': education_level,
                'language_of_service': language_of_service,
                'school_id': school_id,
                'gender': gender,
                'moveToCapitalArea': moveToCapitalArea,
                'tulolaji': tulolaji,
                'monthly_income': monthly_income,
                'Varallisuutta': Varallisuutta,
                'Varallisuusmaara': Varallisuusmaara,
                'lisatiedot': lisatiedot,
                'student_number': student_number,
                'housingSituationSelect': housingSituationSelect,
                'applicationReasonSelect': applicationReasonSelect,
                'accountOfService': accountOfService,
                'Loginemail': Loginemail,
                'Loginpassword': Loginpassword,
                'hometype': hometype,
                'area': area,
                'input_birth_date': input_birth_date,
                'languageOfServicePass': languageOfServicePass,
                'applicationReasonHoaSelect': applicationReasonHoaSelect,
                'completeness': completeness,
                'Makepassword': Makepassword,
                'stateID': stateID,
                'desired_rent': desired_rent,
                'file_path': file_path,
                'file_pathx': file_pathx,
                'file_pathxxxx': file_pathxxxx
            }
            server2_url = 'http://[REDACTED]:5000/run_app'
            # With these lines
            files = {}
            if file_path:
                print('acs')
                files['fileInput'] = (filename, open(file_path, 'rb'))
            if file_pathx:
                files['fileInputx'] = (filenamex, open(file_pathx, 'rb'))
            if file_pathxxxx:
                files['fileInputxxxx'] = (filenamexxxx, open(file_pathxxxx, 'rb'))
            print(files)
            ###response = requests.post(server2_url, data=data, files=files)
            # Check if the response content is JSON
            ###try:
                ###json_response = response.json()
                ###print("Server 2 response:", json_response)
            ###except ValueError:
                ###print("Server 2 response is not JSON")
            # Forward the data and files to Server 2
            # ... (existing code)
            # Forward the data and files to Server 2
            # Handle the response from the Windows laptop
            # Forward the data and files to Server 2
            with processing_lock:
                user_queue.put((data, files))

            # Set the processing status to pending
            with processing_lock:
                processing_status = {"status": "pending", "data": {}}

            # Block until processing is complete
            while not processing_complete:
                time.sleep(1)

            # Reset the processing status for the next request
            with processing_lock:
                processing_complete = False
            ##
            ##queue_length=user_queue.qsize()
            # Return a JSON response indicating success
            if language_of_service=='0':
                return render_template('loadingfi.html', image_path1='static/tryeth.jpg', image_path2='static/trybtc.jpg', language=language_of_service, doeshehaveaccount=accountOfService, completion='yes', quelength=queue_length)
            else:
                return render_template('loadingen.html', image_path1='static/tryeth.jpg', image_path2='static/trybtc.jpg', language=language_of_service, doeshehaveaccount=accountOfService, completion='yes', quelength=queue_length)

            #return jsonify({"status": "success", "queue_length": queue_length})
            
        except Exception as e:
            if language_of_service=='0':
                return render_template('loadingfi.html', image_path1='static/tryeth.jpg', image_path2='static/trybtc.jpg', language=language_of_service, doeshehaveaccount=accountOfService, completion='yes', quelength=queue_length)
            else:
                return render_template('loadingen.html', image_path1='static/tryeth.jpg', image_path2='static/trybtc.jpg', language=language_of_service, doeshehaveaccount=accountOfService, completion='yes', quelength=queue_length)

            #return jsonify({'success': False, 'error': str(e)}), 500

    else:
        return 'Invalid Method'
    

def background_processing():
    global processing_status
    global queue_length
    while True:
        try:
            data, files = user_queue.get()
            print("Processing user request in background:", data)
            result, status_code = process_user_request(data, files)

            if status_code == 200:
                ##queue_length = queue_length - 1
                # Extract relevant information from the response
                image_path1 = result.get('image_path1', '')
                image_path2 = result.get('image_path2', '')
                language_of_service = result.get('language', '')
                completion = result.get('completion', '')
                accountOfService = result.get('accountOfService', '')

                # Extract file paths from the response
                file_path = result.get('file_path', '')
                file_pathx = result.get('file_pathx', '')
                file_pathxxxx = result.get('file_pathxxxx', '')
                print("User request processed successfully")

                # Update the processing status with the response data
                processing_status = {
                    "status": "complete",
                    "data": {
                        "image_path1": image_path1,
                        "image_path2": image_path2,
                        "language_of_service": language_of_service,
                        "completion": completion,
                        "accountOfService": accountOfService,
                        "file_path": file_path,
                        "file_pathx": file_pathx,
                        "file_pathxxxx": file_pathxxxx,
                    }
                }
            else:
                print(f"Error from Windows laptop: {result}, Status Code: {status_code}")
                # Update the processing status with the response data
                processing_status = {"status": "complete", "data": {"error": f"Status Code: {status_code}"}}

        except queue.Empty:
            # Sleep for a while if the queue is empty
            time.sleep(1)

        except Exception as e:
            print(f"Error during background processing: {str(e)}")
            # Update the processing status with the error
            processing_status = {"status": "complete", "data": {"error": str(e)}}

# Start the background processing thread
background_thread = threading.Thread(target=background_processing)
background_thread.start()

# Add the rest of your routes and configurations

@app.route('/')
def index():
    global processing_result
    global template_visit_count
    template_visit_count = template_visit_count + 1

    # Retrieve or create the VisitCount record
    visit_count_record = VisitCount.query.first()
    if not visit_count_record:
        visit_count_record = VisitCount(count=0)
        db.session.add(visit_count_record)

    visit_count_record.count += 1
    db.session.commit()
    ###
    # Check if the result is available
    if processing_result:
        result_key = processing_result.get("result_key")
        error = processing_result.get("error")

        if result_key:
            return render_template('result_template.html', result=result_key)
        elif error:
            return f"Error: {error}", 500

    return render_template('index.html')


# Add a route to get the current queue length
@app.route('/get_queue_length', methods=['GET'])
def get_queue_length():
    global user_queue
    global queue_length 
    #queue_length = user_queue.qsize()
    return jsonify({"queueLength": queue_length})

# Start the background processing thread
##background_thread = threading.Thread(target=background_processing)
##background_thread.start()
# ... (other routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
