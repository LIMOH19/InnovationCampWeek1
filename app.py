from bson.son import re
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.week_one


## HTML 화면 보여주기
@app.route('/')
def main():
    return render_template('main.html')


# 등록하기(POST) API
@app.route('/post', methods=['POST'])
def post_place():
    name_receive = request.form['name_give']
    type_receive = request.form['type_give']
    continent_receive = request.form['continent_give']
    star_receive = request.form['star_give']
    review_receive = request.form['review_give']
    img_url_receive = request.form['img_url_give']
    

    doc = {
        'name': name_receive,
        'type': type_receive,
        'continent': continent_receive,
        'star': star_receive,
        'review': review_receive,
        'img-url': img_url_receive,
    }

    db.restaurants.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


# 주문 목록보기(Read) API
@app.route('/post', methods=['GET'])
def view_places():
    
    places = list(db.restaurants.find({}, {'_id': False}))

    return jsonify({'places': places})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)