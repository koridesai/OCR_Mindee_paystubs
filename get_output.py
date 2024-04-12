import json
import requests

# Load data from the JSON file
with open("paystub_output.json", "r") as json_file:
    response_data = json.load(json_file)

# Reads the ID from the paystub_output.json file
job_id = response_data["job"]["id"]
print("\nJob id is :", job_id)

# Construct the URL for document retrieval
url = f"https://api.mindee.net/v1/products/saikoride1999/us_pay_stubs/v1/documents/queue/{job_id}"
print("\nRequest URL:", url)

# Specify headers with the authorization token
headers = {
    'Authorization': 'Token 24e87821e0b72583dcf4227d98333ff7'
}

# Make the API call with GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse response as JSON
    print("\nResponse data:", data)
    # Write the JSON output to final_output.json
    with open("final_output.json", "w") as final_output_file:
        json.dump(data, final_output_file)
    print("\nFinal output saved to final_output.json")
else:
    print("\nError:", response.status_code, response.reason)