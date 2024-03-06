from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)

@app.route('/')
def hello_world():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',  # Dejar en blanco si no configuraste una contraseña para root
                                 db='mydatabase',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT 'Hello, World!' AS msg"
            cursor.execute(sql)
            result = cursor.fetchone()
            return jsonify(result)
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True port=5080)
