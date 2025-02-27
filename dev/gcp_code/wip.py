import json
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Function to generate a random policy holder address
def generate_address():
    return {
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "postal_code": fake.zipcode(),
        "country": fake.country()
    }

# Function to generate a random beneficiary
def generate_beneficiary():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "relationship": random.choice(["Spouse", "Child", "Parent", "Siblings", "Friend"]),
        "percentage": random.randint(1, 100)
    }

# Function to generate a random insurance policy
def generate_policy():
    policy_id = fake.uuid4()
    policy_holder = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "dob": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
        "address": generate_address()
    }
    policy_type = random.choice(["Life", "Health", "Auto", "Home", "Travel"])
    coverage_amount = round(random.uniform(5000.00, 500000.00), 2)
    premium_amount = round(random.uniform(100.00, 2000.00), 2)
    start_date = fake.date_this_decade().strftime("%Y-%m-%d")
    end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=random.randint(365, 3650))).strftime("%Y-%m-%d")
    
    beneficiaries = [generate_beneficiary() for _ in range(random.randint(1, 3))]  # Randomly assign 1 to 3 beneficiaries

    return {
        "policy_id": policy_id,
        "policy_holder": policy_holder,
        "policy_type": policy_type,
        "coverage_amount": coverage_amount,
        "premium_amount": premium_amount,
        "policy_start_date": start_date,
        "policy_end_date": end_date,
        "beneficiaries": beneficiaries
    }

# Generate 10 sample records and store them in a list
sample_records = [generate_policy() for _ in range(10)]

# Print the list of records
print(sample_records)

# Optionally, you can save them to a file
with open("insurance_policies.json", "w") as f:
    json.dump(sample_records, f, indent=2)

print("Sample records generated and saved to 'insurance_policies.json'")
