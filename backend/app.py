from flask import Flask, json, request
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient('mongodb://192.168.1.155:27017') # set to env var for completion. currently running on secondary machine (LMT-Lap-3)
db = client['testData']
collection = db.test_collection

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "API is fucking working"

@app.route("/get", methods=['GET'])
def get_data():
    try:
        db_data = collection.find()
        response = []
        for item in db_data:
            item['_id'] = str(item['_id'])
            response.append(item)
            
        return json.dumps(response)
    
    except Exception as e:
        return e
    
@app.route("/post", methods=['POST'])
def post_data():
    ins_data = request.get_json()
    
    try:
        try:
            data = collection.insert_many(ins_data)
        except:
            data = collection.insert_one(ins_data)
            
        print("inserting:")
        print(data)
        return str(data)
    
    except Exception as e:
        return json.dumps(e)
        