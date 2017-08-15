from flask_restful import Api, fields, marshal_with, reqparse, Resource
from flask import Blueprint, current_app, request, make_response, Response, g
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(CURRENT_DIR,'..', 'config')

proxy = Blueprint('proxy', __name__, url_prefix='/proxy')


class Proxy(Resource):

    # def post(self):
    #     req = request.get_data().decode()
    #     response = methods.dispatch(req)
    #     return Response(str(response), response.http_status,
    #                     mimetype='application/json')

    def get(self):

        return '1'

api = Api(proxy)
api.add_resource(Proxy, "")