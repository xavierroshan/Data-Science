import json
import random
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Number of files and records per file
num_files = 10
records_per_file = 500

# Function to generate random insurance policy data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        policy_id = fake.uuid4()
        policy_holder_name = fake.name()
        policy_holder_address = fake.address().replace("\n", ", ")
        policy_type = random.choice(["Life", "Health", "Auto", "Home", "Travel"])
        policy_start_date = fake.date_this_decade()
        policy_end_date = fake.date_between(start_date=policy_start_date, end_date="+10y")
        coverage_amount = round(random.uniform(50000, 1000000), 2)
        premium_amount = round(coverage_amount * random.uniform(0.01, 0.05), 2)  # 1% - 5% of coverage
        payment_frequency = random.choice(["Monthly", "Quarterly", "Annually"])
        policy_status = random.choice(["Active", "Expired", "Claimed", "Suspended"])
        beneficiary_name = fake.name() if random.random() > 0.2 else None  # 80% chance to have a beneficiary
        claim_history = [
            {
                "claim_id": fake.uuid4(),
                "claim_date": fake.date_this_decade().isoformat(),
                "claim_amount": round(random.uniform(1000, 50000), 2),
                "claim_status": random.choice(["Approved", "Pending", "Denied"])
            }
        ] if random.random() > 0.5 else []  # 50% chance to have claim history

        data.append({
            "policy_id": policy_id,
            "policy_holder_name": policy_holder_name,
            "policy_holder_address": policy_holder_address,
            "policy_type": policy_type,
            "policy_start_date": policy_start_date.isoformat(),
            "policy_end_date": policy_end_date.isoformat(),
            "coverage_amount": coverage_amount,
            "premium_amount": premium_amount,
            "payment_frequency": payment_frequency,
            "policy_status": policy_status,
            "beneficiary_name": beneficiary_name,
            "claim_history": claim_history
        })

    return data

# Generate and save 10 JSON files
for i in range(1, num_files + 1):
    file_name = f"insurance_policies_{i}.json"
    
    # Generate random records
    records = generate_data(records_per_file)
    
    # Write data to JSON file
    with open(file_name, "w") as out_file:
        json.dump(records, out_file, indent=4)
    
    print(f"Generated {file_name} with {records_per_file} records.")

print("JSON files created successfully!")