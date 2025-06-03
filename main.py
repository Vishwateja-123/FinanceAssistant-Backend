import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns the port
    app.run(host="0.0.0.0", port=port)
