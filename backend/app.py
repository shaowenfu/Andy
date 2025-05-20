"""
Flask入口，负责API路由和请求分发
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from core.orchestrator import Orchestrator

app = Flask(__name__)
CORS(app)
orchestrator = Orchestrator()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('input', '')
    response = orchestrator.handle_input(user_input)
    return jsonify({'result': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
