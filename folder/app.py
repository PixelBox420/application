# app.py (first server)
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

second_server_url = "http://[REDACTED]:5000/upload_endpoint"  # Update with the correct URL of the second server

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    form_field_1 = request.form.get('form_field_1')
    form_field_2 = request.form.get('form_field_2')

    file_1 = request.files.get('file_1')
    file_2 = request.files.get('file_2')

   # print(f"Received Form Data: Form Field 1: {form_field_1}, Form Field 2: {form_field_2}")
   # print(f"Received File Data: File 1: {file_1.filename if file_1 else 'N/A'}, File 2: {file_2.filename if file_2 else 'N/A'}")

    # Sending data to the second server
    data = {'form_field_1': form_field_1, 'form_field_2': form_field_2}
    
    files = {}
    if file_1:
        files['file_1'] = (file_1.filename, file_1)
    if file_2:
        files['file_2'] = (file_2.filename, file_2)

   # print("Sending Data to Second Server:", data)
   # print("Sending Files to Second Server:", files)

    try:
        response = requests.post(second_server_url, data=data, files=files)
        response.raise_for_status()
       # print("Second Server Response:", response.text)
        result = response.json()
        return jsonify(result=result)

    except requests.exceptions.RequestException as e:
       # print("Error connecting to the second server:", e)
        return jsonify(error=str(e))
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
