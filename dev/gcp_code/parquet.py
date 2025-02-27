import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import random
from faker import Faker

#Define parquet schema
schema = pa.schema([
    pa.field("order_id", pa.string()),
    pa.field("product_id", pa.string()),
    pa.field("product_name", pa.string()),
    pa.field("category", pa.string()),
    pa.field("supplier_id", pa.string()),
    pa.field("supplier_name", pa.string()),
    pa.field("order_date", pa.date32()),
    pa.field("shipment_date", pa.timestamp("us")),
    pa.field("quantity_ordered", pa.int32()),
    pa.field("unit_price", pa.float64()),
    pa.field("total_cost", pa.float64()),
    pa.field("currency", pa.string()),
    pa.field("status", pa.string()),
    pa.field("warehouse_location", pa.string()),
    pa.field("shipment_tracking", pa.string()),
    pa.field("supplier_contact", pa.struct([
        pa.field("contact_name", pa.string()),
        pa.field("email", pa.string()),
        pa.field("phone", pa.string())
    ])),
    pa.field("shipment_details", pa.struct([
        pa.field("carrier", pa.string()),
        pa.field("tracking_number", pa.string()),
        pa.field("estimated_arrival", pa.timestamp("us")),
        pa.field("shipment_status", pa.string())
    ]))
])

#Get the records for the parquet file
records = [
    ["ORD123456", "PROD987654", "Wireless Mouse", "Electronics", "SUP001", "Tech Supplies Inc.", pd.to_datetime("2025-02-26").date(), pd.to_datetime("2025-02-28 14:35:00"), 10, 25.99, 259.90, "USD", "Shipped", "WH-A5-2", "TRACK123456789", {"contact_name": "John Doe", "email": "john.doe@techsupplies.com", "phone": "+1234567890"}, {"carrier": "FedEx", "tracking_number": "FDX987654321", "estimated_arrival": pd.to_datetime("2025-03-02 10:00:00"), "shipment_status": "In Transit"}],
    ["ORD123457", "PROD987655", "Bluetooth Keyboard", "Electronics", "SUP002", "Gadget World", pd.to_datetime("2025-02-26").date(), pd.to_datetime("2025-02-28 15:35:00"), 15, 45.50, 682.50, "USD", "Shipped", "WH-A5-3", "TRACK123456790", {"contact_name": "Alice Green", "email": "alice.green@gadgetworld.com", "phone": "+1234567891"}, {"carrier": "UPS", "tracking_number": "UPS987654322", "estimated_arrival": pd.to_datetime("2025-03-02 12:00:00"), "shipment_status": "In Transit"}],
    ["ORD123458", "PROD987656", "Laptop Stand", "Furniture", "SUP003", "Office Supplies Co.", pd.to_datetime("2025-02-25").date(), pd.to_datetime("2025-02-28 16:30:00"), 8, 15.75, 126.00, "USD", "Shipped", "WH-A5-4", "TRACK123456791", {"contact_name": "Bob White", "email": "bob.white@officesuppliesco.com", "phone": "+1234567892"}, {"carrier": "DHL", "tracking_number": "DHL987654323", "estimated_arrival": pd.to_datetime("2025-03-03 14:00:00"), "shipment_status": "In Transit"}],
    ["ORD123459", "PROD987657", "Office Chair", "Furniture", "SUP004", "Comfort Seating", pd.to_datetime("2025-02-25").date(), pd.to_datetime("2025-02-28 17:00:00"), 5, 150.00, 750.00, "USD", "Shipped", "WH-A5-5", "TRACK123456792", {"contact_name": "Carol Black", "email": "carol.black@comfortseating.com", "phone": "+1234567893"}, {"carrier": "FedEx", "tracking_number": "FDX987654324", "estimated_arrival": pd.to_datetime("2025-03-04 10:00:00"), "shipment_status": "In Transit"}],
    ["ORD123460", "PROD987658", "Smartphone", "Electronics", "SUP005", "Mobile World", pd.to_datetime("2025-02-26").date(), pd.to_datetime("2025-03-01 09:00:00"), 20, 599.99, 11999.80, "USD", "Shipped", "WH-A5-6", "TRACK123456793", {"contact_name": "Dave Blue", "email": "dave.blue@mobileworld.com", "phone": "+1234567894"}, {"carrier": "UPS", "tracking_number": "UPS987654325", "estimated_arrival": pd.to_datetime("2025-03-05 16:00:00"), "shipment_status": "In Transit"}],
    ["ORD123461", "PROD987659", "Tablet", "Electronics", "SUP006", "Gadget Galaxy", pd.to_datetime("2025-02-26").date(), pd.to_datetime("2025-03-01 10:00:00"), 12, 249.99, 2999.88, "USD", "Shipped", "WH-A5-7", "TRACK123456794", {"contact_name": "Eva Brown", "email": "eva.brown@gadgetgalaxy.com", "phone": "+1234567895"}, {"carrier": "DHL", "tracking_number": "DHL987654326", "estimated_arrival": pd.to_datetime("2025-03-06 11:00:00"), "shipment_status": "In Transit"}],
    ["ORD123462", "PROD987660", "Gaming Mouse", "Electronics", "SUP007", "Game On", pd.to_datetime("2025-02-27").date(), pd.to_datetime("2025-03-02 11:00:00"), 18, 79.99, 1439.82, "USD", "Shipped", "WH-A5-8", "TRACK123456795", {"contact_name": "Frank Red", "email": "frank.red@gameon.com", "phone": "+1234567896"}, {"carrier": "FedEx", "tracking_number": "FDX987654327", "estimated_arrival": pd.to_datetime("2025-03-07 13:00:00"), "shipment_status": "In Transit"}],
    ["ORD123463", "PROD987661", "4K Monitor", "Electronics", "SUP008", "Tech Vision", pd.to_datetime("2025-02-27").date(), pd.to_datetime("2025-03-02 12:00:00"), 7, 349.99, 2449.93, "USD", "Shipped", "WH-A5-9", "TRACK123456796", {"contact_name": "Grace Yellow", "email": "grace.yellow@techvision.com", "phone": "+1234567897"}, {"carrier": "UPS", "tracking_number": "UPS987654328", "estimated_arrival": pd.to_datetime("2025-03-08 15:00:00"), "shipment_status": "In Transit"}],
    ["ORD123464", "PROD987662", "Wireless Headphones", "Electronics", "SUP009", "SoundWave", pd.to_datetime("2025-02-28").date(), pd.to_datetime("2025-03-03 13:00:00"), 25, 199.99, 4999.75, "USD", "Shipped", "WH-A5-10", "TRACK123456797", {"contact_name": "Helen Pink", "email": "helen.pink@soundwave.com", "phone": "+1234567898"}, {"carrier": "DHL", "tracking_number": "DHL987654329", "estimated_arrival": pd.to_datetime("2025-03-09 14:00:00"), "shipment_status": "In Transit"}],
    ["ORD123465", "PROD987663", "Portable Charger", "Electronics", "SUP010", "PowerUp", pd.to_datetime("2025-02-28").date(), pd.to_datetime("2025-03-03 14:00:00"), 30, 39.99, 1199.70, "USD", "Shipped", "WH-A5-11", "TRACK123456798", {"contact_name": "Ivy Orange", "email": "ivy.orange@powerup.com", "phone": "+1234567899"}, {"carrier": "FedEx", "tracking_number": "FDX987654330", "estimated_arrival": pd.to_datetime("2025-03-10 16:00:00"), "shipment_status": "In Transit"}]
]


print(records)


# # Create a DataFrame
df = pd.DataFrame(records, columns=schema.names)

# # Convert to Arrow Table
table = pa.Table.from_pandas(df, schema=schema)

#  # Save as Parquet file
pq.write_table(table, "file_name")