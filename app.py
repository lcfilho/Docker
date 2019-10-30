from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='luis123',
                             db='TCP',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['POST'])
def get_pessoa_post():

    cursor = connection.cursor()

    if request.method == 'POST':
        data = request.json
        cursor.execute('SELECT * FROM TCP WHERE cpf = {}'.format(data['cpf']))

    return jsonify(cursor.fetchone())

@app.route('/<string:cpf>', methods=['GET'])
def get_pessoa(cpf):

    cursor = connection.cursor()

    if request.method == 'GET':
        data = request.json
        cursor.execute('SELECT * FROM TCP WHERE cpf = {}'.format(cpf))

    return jsonify(cursor.fetchone())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
