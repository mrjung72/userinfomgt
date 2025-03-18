from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "sahara",
    "password": "1111",
    "database": "userinfodb",
    "port": 3306,
    "cursorclass": pymysql.cursors.DictCursor
}

@app.route("/users", methods=["GET"])
def get_users():
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return jsonify(users)  # JSON 반환
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
