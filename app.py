from flask import Flask, request, render_template
import requests
import json
import time
import subprocess
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

API_URL = "https://api.mindee.net/v1/products/saikoride1999/us_pay_stubs/v1/predict_async"
API_KEY = "24e87821e0b72583dcf4227d98333ff7"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', message="No file part")
        
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('upload.html', message="No selected file")

        if file:
            # Save the uploaded file
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # Process the uploaded file
            with open(filename, "rb") as myfile:
                files = {"document": myfile}
                headers = {"Authorization": "Token " + API_KEY}
                response = requests.post(API_URL, files=files, headers=headers)
                response_data = response.json()

            # Write response data to a JSON file
            output_file = "paystub_output.json"
            with open(output_file, "w") as json_file:
                json.dump(response_data, json_file)

            print("\nOutput saved to", output_file)

            time.sleep(5)

            # Call the get_output.py script
            subprocess.run(["python", "get_output.py"])

            time.sleep(2)

            # Call the extract_data.py script
            subprocess.run(["python", "extract_data.py"])

            return render_template('upload.html', message="File uploaded and processed successfully")

    return render_template('upload.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
