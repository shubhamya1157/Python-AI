'''

from flask import Flask,jsonify,request

app = Flask(__name__)

data = {"name": "shubham",
"age":18}

@app.route("/")
def home():
    return "welcome to my server"

@app.route("/get",methods = ["GET"])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True,port= 1157)

'''    
'''
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["my_data_base"]

collection = db["my_details"]
 
details = {
    "name" : "shubham yadav"
 }
collection.insert_one(details)
# collection.insert_many()
'''
