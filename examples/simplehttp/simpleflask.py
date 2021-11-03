from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def sample():
    received = request.get_json()
    return received, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999)
