from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers.usercontroller import BlueprintUser  # Asegúrate de importar el blueprint



#API
app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(BlueprintUser)

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
    