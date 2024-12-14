from pymongo import MongoClient

def get_db():
    //client = MongoClient("mongodb+srv://nesnukurian:pragra@cluster0.alurz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    client = MongoClient("mongodb+srv://harkaur02:lLfoMtnTJ0ze3JVy@cluster0.2sboz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['ecommerce_db'] 
    return db 
            

def insert_static_data():
    db = get_db()
    products_collection = db['products']
    if products_collection.count_documents({}) == 0: 
        static_products = [
            {"name": "Laptop", "description": "A high-performance laptop.", "price": 1200, "stock": 10},
            {"name": "Smartphone", "description": "Latest model smartphone.", "price": 800, "stock": 15},
            {"name": "Headphones", "description": "Noise-cancelling headphones.", "price": 150, "stock": 30},
            {"name": "Smart Watch", "description": "A watch with fitness tracking.", "price": 200, "stock": 20}
        ]
        products_collection.insert_many(static_products)
        print("Inserted static products data.")

    # Insert users data if collection is empty
    users_collection = db['users']
    if users_collection.count_documents({}) == 0: 
        static_users = [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "securepassword"},
            {"username": "alice_jones", "email": "alice@example.com", "password": "alicepass"},
            {"username": "bob_williams", "email": "bob@example.com", "password": "bobpass"}
        ]
        users_collection.insert_many(static_users)
        print("Inserted static users data.")
