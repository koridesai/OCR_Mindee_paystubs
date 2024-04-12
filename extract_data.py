import json

# Load data from final_output.json
with open("final_output.json", "r") as json_file:
    data = json.load(json_file)

# Extract relevant details
document_info = data["document"]["inference"]["prediction"]

# Print extracted details
print("\nExtracted details from the document:\n\n")
print("Employer:", document_info["employer"]["value"])
print("Net pay:", document_info["net_pay"]["value"])
print("Pay date:", document_info["pay_date"]["value"])
print("Period beginning:", document_info["period_beginning"]["value"])
print("Period ending:", document_info["period_ending"]["value"])
print("Gross pay:", document_info["gross_pay"]["value"])
print("Total tax:", document_info["total_tax"]["value"])
