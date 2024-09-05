from flask import Flask, request, jsonify
from flask_cors import CORS

#API
app = Flask(__name__)
cors = CORS(app)


if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
    
@app.route('/')
def hello_world():
    return '<1> Hello, World! </1>'