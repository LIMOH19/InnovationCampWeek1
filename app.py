from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('mongodb+srv://WOP:worldplate@cluster0.n5aphnb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbwop



@app.route('/')
def main():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기

    return render_template("detail.html")
#
#
# @app.route('/register', methods=['POST'])
# def save_restaurant():
#     # 단어 저장하기
#     name_receive = request.form['name_give']
#     star_receive = request.form['star_give']
#     food_receive = request.form['food_give']
#     comment_receive = request.form['comment_give']
#
#     doc = {'name': name_receive,
#            'star': star_receive,
#            'food': food_receive,
#            'comment': comment_receive
#     }
#     db.register.insert_one(doc)
#     return jsonify({'result': 'success', 'msg': '등록 완료'})

@app.route("/detail", methods=["GET"])
def search_rest():
    # doc = []
    # store_receive = request.args.get('rest_give')
    # stores = list(db.register.find({}, {'_id': False}))
    # # for store in stores:
    # #     if store_receive in store['name']:
    # #         doc.append(store)
    # # search_list = {'search_list':doc}
    return jsonify({'search_list': search_list, 'msg': '검색 완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)