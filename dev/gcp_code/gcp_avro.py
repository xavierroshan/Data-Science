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

# Updated records: now as dictionaries instead of lists
records = [
    {
        "transaction_id": '123e4567-e89b-12d3-a456-426614174000',
        "account_number": 'GB29XABC10161234567801',
        "account_holder": 'John Doe',
        "bank_name": 'ACME Bank',
        "transaction_type": 'Deposit',
        "transaction_amount": 253.76,
        "currency": 'USD',
        "transaction_date": 1637178329000,
        "transaction_status": 'Success',
        "merchant_details": {'merchant_name': 'TechStore', 'merchant_category': 'Electronics'},
        "location": 'London',
        "reference_number": 'c9b9b2ad-b5b7-4b85-b8d7-0e71b96bc3a3',
        "remarks": 'Payment for invoice #12345'
    },
    {
        "transaction_id": '789e4567-e89b-12d3-a456-426614174001',
        "account_number": 'DE44XABC10161234567802',
        "account_holder": 'Jane Smith',
        "bank_name": 'Global Bank',
        "transaction_type": 'Withdrawal',
        "transaction_amount": 500.65,
        "currency": 'EUR',
        "transaction_date": 1637178345000,
        "transaction_status": 'Failed',
        "merchant_details": None,
        "location": 'Paris',
        "reference_number": None,
        "remarks": 'Failed transaction, insufficient funds'
    },
    {
        "transaction_id": '456e4567-e89b-12d3-a456-426614174002',
        "account_number": 'US34XABC10161234567803',
        "account_holder": 'Alice Brown',
        "bank_name": 'American Bank',
        "transaction_type": 'Transfer',
        "transaction_amount": 1000.0,
        "currency": 'USD',
        "transaction_date": 1637178361000,
        "transaction_status": 'Success',
        "merchant_details": {'merchant_name': 'MegaRetail', 'merchant_category': 'Retail'},
        "location": 'New York',
        "reference_number": 'f1b1b2ad-b5b7-4b85-b8d7-1e71b96bc3a4',
        "remarks": 'Transfer for invoice #67890'
    },
    # ... other records
]

# Open and write the Avro file
with open("/home/roshan/python_dev/Data-Science/dev/gcp_code/gcp_avro.avro", "wb") as f:
    fastavro.writer(f, avro_schema, records)

print("Avro file created successfully!")
