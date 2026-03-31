from flask import Flask, request, jsonify

app = Flask(__name__)
data = []

@app.route('/data', methods=['POST'])
def receive():
    d = request.json
    data.append(d)

    if d['temp'] > 30:
        print("⚠️ ALERT!")

    return {"msg": "ok"}

@app.route('/data', methods=['GET'])
def send():
    return jsonify(data)

app.run(debug=True)
