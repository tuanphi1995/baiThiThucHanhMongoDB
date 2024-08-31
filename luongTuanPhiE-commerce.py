from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client['eShop']  # Database name
collection = db['OrderCollection']  # Collection name

# Sample data
order_data = {
    "orderid": 1,
    "products": [
        {
            "product_id": "quannau",
            "product_name": "trousers",
            "size": "XL",
            "price": 10,
            "quantity": 1
        },
        {
            "product_id": "somi",
            "product_name": "shirt",
            "size": "XL",
            "price": 10.5,
            "quantity": 2
        }
    ],
    "total_amount": 31,
    "delivery_address": "Hanoi"
}

# Insert data into the collection
collection.insert_one(order_data)
print("Order inserted successfully!")

# Edit delivery address by orderid
collection.update_one({"orderid": 1}, {"$set": {"delivery_address": "New York"}})
print("Delivery address updated successfully!")

# Remove an order by orderid
collection.delete_one({"orderid": 1})
print("Order deleted successfully!")

# Insert multiple orders
orders = [
    {
        "orderid": 2,
        "products": [
            {
                "product_id": "jeans",
                "product_name": "denim",
                "size": "L",
                "price": 20,
                "quantity": 2
            }
        ],
        "total_amount": 40,
        "delivery_address": "Los Angeles"
    },
    {
        "orderid": 3,
        "products": [
            {
                "product_id": "jacket",
                "product_name": "leather jacket",
                "size": "M",
                "price": 50,
                "quantity": 1
            }
        ],
        "total_amount": 50,
        "delivery_address": "Chicago"
    }
]

collection.insert_many(orders)
print("Multiple orders inserted successfully!")

# Read all orders
orders = collection.find()
print("All orders:")
for order in orders:
    print(order)

# Calculate total amount of a specific order
specific_order = collection.find_one({"orderid": 2})
if specific_order:
    print(f"Total amount for order 2: {specific_order['total_amount']}")

# Count total product_id equal to "somi"
somi_count = collection.count_documents({"products.product_id": "somi"})
print(f"Total products with product_id 'somi': {somi_count}")
