from flask import Flask, Blueprint, redirect
from flask_restplus import Api
from flask_cors import CORS
from app_core import config
from endpoints import ml_endpoint


app = Flask(__name__)
CORS(app)

__api_prefix = '/api'

blueprint = Blueprint('api', __name__, url_prefix=__api_prefix)
api = Api(blueprint, version='1.0', title='Python and TensorFlow WebServer API',
          description='Example of Python and TensorFlow WebServer API')
api.add_namespace(ml_endpoint.instance)
app.register_blueprint(blueprint)


@app.route('/')
def core():
    return redirect(__api_prefix)


def main():
    if config is not None:
        app.run(debug=True, host=config.host, port=config.port)


if __name__ == '__main__':
    main()