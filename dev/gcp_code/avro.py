import json
import random
import fastavro
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Number of files and records per file
num_files = 10
records_per_file = 500

# Define Avro Schema for Banking Transactions
avro_schema = {
    "type": "record",
    "name": "BankTransaction",
    "namespace": "com.example.banking",
    "fields": [
        {"name": "transaction_id", "type": "string"},
        {"name": "account_number", "type": "string"},
        {"name": "account_holder", "type": "string"},
        {"name": "bank_name", "type": "string"},
        {"name": "transaction_type", "type": {"type": "enum", "name": "TransactionType", "symbols": ["Deposit", "Withdrawal", "Transfer", "Payment"]}},
        {"name": "transaction_amount", "type": "float"},
        {"name": "currency", "type": "string"},
        {"name": "transaction_date", "type": "long", "logicalType": "timestamp-millis"},
        {"name": "transaction_status", "type": {"type": "enum", "name": "TransactionStatus", "symbols": ["Success", "Failed", "Pending"]}},
        {"name": "merchant_details", "type": ["null", 
            {
                "type": "record",
                "name": "MerchantDetails",
                "fields": [
                    {"name": "merchant_name", "type": "string"},
                    {"name": "merchant_category", "type": "string"}
                ]
            }
        ], "default": None},
        {"name": "location", "type": "string"},
        {"name": "reference_number", "type": ["null", "string"], "default": None},
        {"name": "remarks", "type": ["null", "string"], "default": None}
    ]
}

# Function to generate random banking transaction data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        account_number = fake.bban()
        account_holder = fake.name()
        bank_name = random.choice(["Bank of America", "Chase", "Wells Fargo", "CitiBank", "HSBC"])
        transaction_type = random.choice(["Deposit", "Withdrawal", "Transfer", "Payment"])
        transaction_amount = round(random.uniform(10, 5000), 2)
        currency = random.choice(["USD", "EUR", "GBP", "INR"])
        transaction_date = int(fake.date_time_this_year().timestamp() * 1000)  # Convert to milliseconds
        transaction_status = random.choice(["Success", "Failed", "Pending"])
        location = fake.city()

        # Merchant details only for "Payment" transactions
        merchant_details = None
        if transaction_type == "Payment":
            merchant_details = {
                "merchant_name": fake.company(),
                "merchant_category": random.choice(["Retail", "E-commerce", "Food", "Travel", "Electronics"])
            }

        reference_number = fake.uuid4() if random.random() > 0.2 else None  # 80% chance of having a reference
        remarks = fake.sentence() if random.random() > 0.5 else None  # 50% chance of having remarks

        data.append({
            "transaction_id": transaction_id,
            "account_number": account_number,
            "account_holder": account_holder,
            "bank_name": bank_name,
            "transaction_type": transaction_type,
            "transaction_amount": transaction_amount,
            "currency": currency,
            "transaction_date": transaction_date,
            "transaction_status": transaction_status,
            "merchant_details": merchant_details,
            "location": location,
            "reference_number": reference_number,
            "remarks": remarks
        })

    return data

# Generate and save 10 Avro files
for i in range(1, num_files + 1):
    file_name = f"bank_transactions_{i}.avro"
    
    # Generate random records
    records = generate_data(records_per_file)
    
    # Write data to Avro file
    with open(file_name, "wb") as out_file:
        fastavro.writer(out_file, avro_schema, records)
    
    print(f"Generated {file_name} with {records_per_file} records.")

print("Avro files created successfully!")