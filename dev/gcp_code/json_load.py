import json

# List of insurance policy records
records = [
    {'policy_id': '54e1fd6d-5ffc-423f-91b8-9ed43adb543b', 'policy_holder': {'first_name': 'Sarah', 'last_name': 'Ortiz', 'dob': '1956-12-07', 'address': {'street': '5063 Hill Harbor Apt. 162', 'city': 'New Fernando', 'state': 'New York', 'postal_code': '96805', 'country': 'Netherlands'}}, 'policy_type': 'Health', 'coverage_amount': 365704.75, 'premium_amount': 1893.25, 'policy_start_date': '2022-05-16', 'policy_end_date': '2025-01-28', 'beneficiaries': [{'first_name': 'Tracey', 'last_name': 'Hall', 'relationship': 'Parent', 'percentage': 63}]},
    {'policy_id': 'd1aaf081-8ae7-47da-b00a-213bf2728078', 'policy_holder': {'first_name': 'Gabriel', 'last_name': 'Wang', 'dob': '1963-04-30', 'address': {'street': '0702 Joshua Corners Apt. 536', 'city': 'Garzachester', 'state': 'New York', 'postal_code': '97049', 'country': 'Egypt'}}, 'policy_type': 'Auto', 'coverage_amount': 57298.99, 'premium_amount': 1405.57, 'policy_start_date': '2024-05-14', 'policy_end_date': '2028-07-22', 'beneficiaries': [{'first_name': 'Angela', 'last_name': 'Miller', 'relationship': 'Spouse', 'percentage': 4}, {'first_name': 'Christopher', 'last_name': 'Maxwell', 'relationship': 'Parent', 'percentage': 81}, {'first_name': 'Glenn', 'last_name': 'Heath', 'relationship': 'Friend', 'percentage': 9}]},
    {'policy_id': '2e19b714-dd9d-47e7-a956-e6fcf62325bc', 'policy_holder': {'first_name': 'Christopher', 'last_name': 'Coffey', 'dob': '1947-11-08', 'address': {'street': '0058 Sarah Court', 'city': 'New Bradley', 'state': 'South Carolina', 'postal_code': '95204', 'country': 'Serbia'}}, 'policy_type': 'Health', 'coverage_amount': 202446.98, 'premium_amount': 227.82, 'policy_start_date': '2020-04-14', 'policy_end_date': '2022-08-27', 'beneficiaries': [{'first_name': 'Meagan', 'last_name': 'Hayden', 'relationship': 'Child', 'percentage': 68}]},
    {'policy_id': '29d6be42-ce85-42f2-a665-2e7b50f7f3f4', 'policy_holder': {'first_name': 'Chad', 'last_name': 'Edwards', 'dob': '1970-09-05', 'address': {'street': '965 Barker Lodge Suite 683', 'city': 'Danielview', 'state': 'Indiana', 'postal_code': '35536', 'country': 'British Virgin Islands'}}, 'policy_type': 'Health', 'coverage_amount': 246779.06, 'premium_amount': 368.09, 'policy_start_date': '2023-02-24', 'policy_end_date': '2033-01-07', 'beneficiaries': [{'first_name': 'Roberto', 'last_name': 'Levy', 'relationship': 'Spouse', 'percentage': 78}, {'first_name': 'Stacey', 'last_name': 'Valencia', 'relationship': 'Siblings', 'percentage': 18}, {'first_name': 'Annette', 'last_name': 'Gordon', 'relationship': 'Siblings', 'percentage': 22}]},
    {'policy_id': '69ae6fa9-9e4e-47c7-a067-de632ce7f147', 'policy_holder': {'first_name': 'Amanda', 'last_name': 'Jones', 'dob': '2002-09-29', 'address': {'street': '07555 Soto Court', 'city': 'North Madelinefurt', 'state': 'Wisconsin', 'postal_code': '51196', 'country': 'Equatorial Guinea'}}, 'policy_type': 'Travel', 'coverage_amount': 429465.71, 'premium_amount': 1659.69, 'policy_start_date': '2023-03-05', 'policy_end_date': '2025-08-13', 'beneficiaries': [{'first_name': 'Samantha', 'last_name': 'Jones', 'relationship': 'Parent', 'percentage': 44}, {'first_name': 'Christopher', 'last_name': 'Pace', 'relationship': 'Child', 'percentage': 4}]},
    {'policy_id': '5707d54a-8f9e-4692-b4ad-3ccc697a3163', 'policy_holder': {'first_name': 'Austin', 'last_name': 'Martinez', 'dob': '1978-02-04', 'address': {'street': '1495 Karen Knoll Apt. 870', 'city': 'Evansshire', 'state': 'Idaho', 'postal_code': '44835', 'country': 'Maldives'}}, 'policy_type': 'Auto', 'coverage_amount': 201562.15, 'premium_amount': 1979.48, 'policy_start_date': '2023-09-18', 'policy_end_date': '2025-03-12', 'beneficiaries': [{'first_name': 'Sara', 'last_name': 'Rodriguez', 'relationship': 'Spouse', 'percentage': 14}, {'first_name': 'Devin', 'last_name': 'Garner', 'relationship': 'Child', 'percentage': 32}]},
    {'policy_id': 'cff141e9-d6b4-4032-906e-0e2e7e9e5e41', 'policy_holder': {'first_name': 'Regina', 'last_name': 'Garza', 'dob': '1953-06-28', 'address': {'street': '222 Navarro Falls', 'city': 'Lake Sarahmouth', 'state': 'Hawaii', 'postal_code': '79660', 'country': 'Jamaica'}}, 'policy_type': 'Home', 'coverage_amount': 447494.9, 'premium_amount': 1690.44, 'policy_start_date': '2020-05-10', 'policy_end_date': '2030-01-05', 'beneficiaries': [{'first_name': 'Joanna', 'last_name': 'Snyder', 'relationship': 'Friend', 'percentage': 99}, {'first_name': 'Tony', 'last_name': 'Arnold', 'relationship': 'Parent', 'percentage': 31}, {'first_name': 'Maria', 'last_name': 'Cook', 'relationship': 'Siblings', 'percentage': 32}]},
    {'policy_id': '82313752-fd47-476b-8b56-33098c6ed185', 'policy_holder': {'first_name': 'Melanie', 'last_name': 'Roberts', 'dob': '1950-10-04', 'address': {'street': '6949 Calvin Turnpike Apt. 591', 'city': 'Jonesborough', 'state': 'Montana', 'postal_code': '01200', 'country': 'Saint Vincent and the Grenadines'}}, 'policy_type': 'Travel', 'coverage_amount': 462132.89, 'premium_amount': 922.17, 'policy_start_date': '2021-01-01', 'policy_end_date': '2026-05-07', 'beneficiaries': [{'first_name': 'Lori', 'last_name': 'Barnes', 'relationship': 'Parent', 'percentage': 70}]},
]

# Specify the path to the output JSON file
output_file_path = 'insurance_policies.json'

# Writing the records to the JSON file
with open(output_file_path, 'w') as json_file:
    json.dump(records, json_file, indent=4)

print(f"JSON file has been generated at: {output_file_path}")
