from flask import Flask, make_response
from flask_apispec import FlaskApiSpec
from flask_restful import Resource, Api

from .docs import config_doc_spec
from .routes import users

app = Flask(__name__)
api = Api(app)


# noinspection PyMethodMayBeStatic
class Root(Resource):
    def get(self):
        env = app.config['ENV']
        response = make_response(f"Hello from Flask App! (ENV: {env})", 200)
        response.mimetype = "text/plain"
        return response


api.add_resource(Root, '/')
api.add_resource(users.UsersRoot, '/users')
api.add_resource(users.UsersById, '/users/<int:user_id>')

config_doc_spec(app)
docs = FlaskApiSpec(app)
docs.register(users.UsersRoot)
docs.register(users.UsersById)

