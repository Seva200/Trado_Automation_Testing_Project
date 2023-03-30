import time

import pymongo
from urllib.parse import quote
from bson import ObjectId

# Credentials
password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
id_user = "6419adfac122f37221c04509"

def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db

def get_specific_key_value(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value = document.get(key)
        return value
    else:
        return None

def sms_code():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    num_code = get_specific_key_value(db, "users", id_user, "loginCode")
    return num_code


