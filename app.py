from flask import Flask, request, jsonify

app = Flask(__name__)

# Store latest values
latest_data = {"temperature": None, "humidity": None}

@app.route("/", methods=["GET", "POST"])
def home():
    global latest_data
    if request.method == "POST":
        data = request.get_json()
        if not data or "temperature" not in data or "humidity" not in data:
            return jsonify({"error": "Invalid data"}), 400
        latest_data = data
        return jsonify({"status": "Data received"}), 200
    else:
        return jsonify(latest_data)
