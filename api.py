from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API Running ✅"

@app.route('/number')
def number():
    num = request.args.get('num')

    db = {
        "9998887779": {
            "name": "Radhe Gupta",
            "city": "Mithapur"
        }
    }

    if num in db:
        return jsonify({"status": "success", "data": db[num]})
    else:
        return jsonify({"status": "not found"})

app.run(host="0.0.0.0", port=10000)
