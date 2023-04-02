import pymongo
from urllib.parse import quote
from bson import ObjectId

password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
object_id = "6419adfac122f37221c04509"



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

def get_specific_key_value_by_order_number(db, collection_name, order_number, key):
    collection = db[collection_name]
    document = collection.find_one({'number': order_number})
    if document:
        value = document.get(key)
        return value
    else:
        return None


def get_email():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    email = get_specific_key_value(db, "users", object_id, 'email')
    return email

def get_user_id():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    user_id = get_specific_key_value(db, "users", object_id, 'userId')
    return user_id

def get_order_status(order_number):
    db = create_mongo_connection(user_name, encoded_password, db_name)
    status = get_specific_key_value_by_order_number(db, 'orders', order_number, 'status')
    return status

