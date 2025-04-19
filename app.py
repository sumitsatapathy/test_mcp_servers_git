from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/read', methods=['GET'])
def read():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello {name}', 'branch': 'flaskapptest'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'ok', 'message': 'Flask app running on flaskapptest branch'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
