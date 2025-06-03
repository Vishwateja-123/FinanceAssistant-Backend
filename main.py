from flask import Flask, jsonify
from flask_cors import CORS  # ✅ This line enables CORS

app = Flask(__name__)
CORS(app)  # ✅ This allows requests from your frontend

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})
