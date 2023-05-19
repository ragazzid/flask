from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"message": "OK"}), 200


@app.route("/login")
def login():
    return jsonify({"status": "OK"}), 201

if __name__ == '__main__':
    app.run()
