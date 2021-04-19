import os
from flask import Flask, jsonify, redirect
from flask import request, render_template, url_for
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="34.72.13.19",user="root",password="example",db="P9")

@app.route('/api/practica',methods=['GET'])
def cantidad():
    cursor = db.cursor()
    sql = "SELECT * FROM DATOS_P9"
    cursor.execute(sql)
    results = cursor.fetchall()
    dic = {}
    for row in results:
        dic[row[0]]={}
        dic[row[0]]["datos"] = row[1]
    return jsonify(data=dic)



#@app.route('/')
#def hello_world():
#    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)