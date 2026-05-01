from flask import Flask, jsonify

app = Flask(__name__)

@app.route("////api/test")
def test_api():
    return jsonify({"status": "API working"})

app.run()
