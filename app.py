from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:1111@cluster0.wryzw0s.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route("/bucket/rollback", methods=["POST"])
def bucket_rollback(continent):
    continent_receive = request.form['continent']
    review_list = list(db.bucket.find({'continent': continent_receive}, {'_id': False}))
    return jsonify({'reviews': review_list})
