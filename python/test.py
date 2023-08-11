from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def handler():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)