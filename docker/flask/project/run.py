import os,sys
import logging.config
from flask import Flask, g
import flask_login
from flask_pymongo import PyMongo

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(CURRENT_DIR, 'config')

logging.config.fileConfig(os.path.join(config_path, 'logging.conf'))

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

app.logger.logger_name = __name__
app.config.update({
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'test',

})
app.mongo = PyMongo(app, config_prefix='MONGO')

from proxy.routes import proxy, proxy_list
app.register_blueprint(proxy)
app.register_blueprint(proxy_list)


if __name__ == '__main__':
    app.run(debug=True)