from flask import Flask
from flask_cors import CORS
from config import Config
from controllers.usercontroller import BlueprintUser
from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
cors = CORS(app)

app.register_blueprint(BlueprintUser)

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
