from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Python Flask on ECS!', 'version': '1.0'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
