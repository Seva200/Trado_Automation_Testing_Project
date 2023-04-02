import random
import pymongo
from urllib.parse import quote
from bson import ObjectId

password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
phone_num = f'059{random.randint(111111,9999999)}'

def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db

def display_collections(db):
    collections = db.list_collection_names()
    print(f'Collections in {db_name}: {collections}')
    return collections

def get_specific_key_value(db, collection_name, phone_num, key):
    collection = db[collection_name]
    document = collection.find_one({'phone': phone_num})
    if document:
        value = document.get(key)
        return value
    else:
        return None

def code():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    num_code = get_specific_key_value(db, "users", phone_num, "loginCode")
    print(num_code)
    return num_code