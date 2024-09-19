from flask import Flask
from flask_cors import CORS
from config import Config
from controllers.usercontroller import BlueprintUser
from controllers.publicationcontroller import BlueprintPublication
from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
cors = CORS(app)

# Register blueprints
app.register_blueprint(BlueprintUser, url_prefix='/usuarios')
#app.register_blueprint(BlueprintPublication)

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
