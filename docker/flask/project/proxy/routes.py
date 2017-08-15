from flask_restful import Api, fields as fields_restful, marshal_with, reqparse, Resource
from flask import Blueprint, current_app, request, make_response, Response, g
from webargs.flaskparser import parser
from webargs import fields, validate
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(CURRENT_DIR,'..', 'config')

proxy = Blueprint('proxy', __name__, url_prefix='/proxy')
proxy_list = Blueprint('proxy_list', __name__, url_prefix='/proxy_list')

list_type = ['ok', 'ln', 'yandex', 'google', 'bing']


def return_proxy():
    return {"ip": "192.168.0.1"}


def return_proxy_list():
    return {"ip": ["192.168.0.1", "192.168.0.2"]}

user_args = {
    'country': fields.Str(required=False),
    'region': fields.Str(required=False),
    'type_usage': fields.Str(required=False),
    'account': fields.Str(required=False),
    'group': fields.Str(required=False),
    'id': fields.Str(required=False),
}


# resource_fields = {
#     'country':   fields.String,
#     'region':    fields.String,
#     'type_usage':    fields.String,
#     'account':    fields.String,
#     'group':    fields.String,
#     'id':    fields.String,
# }


result = {
    'ip':   fields_restful.String(default="192.168.1.100")
}

# parser_data = reqparse.RequestParser(trim=True)
# parser_data.add_argument('country', type=str, help='Country for this resource')
# parser_data.add_argument('region', type=str, help='Region for this resource')
# parser_data.add_argument('type_usage', type=str, help='Type of usage for this resource')
# parser_data.add_argument('account', type=str, help='Account in social network for this resource')
# parser_data.add_argument('group', type=str, help='Group in social network for this resource')
# parser_data.add_argument('id', type=int, help='Id proxy')
#args = parser_data.parse_args()


class Proxy(Resource):

    def post(self, **kwargs):
        args = parser.parse(user_args, request)
        if 'type_usage' in kwargs:
            if kwargs['type_usage'] in list_type:
                args.update(kwargs)
            else:
                return {"error": "type of usage proxy not exist"}, 404
        # current_app.logger.debug(args)
        return return_proxy(), 201

    def get(self, **kwargs):
        args = parser.parse(user_args, request)
        if 'type_usage' in kwargs:
            if kwargs['type_usage'] in list_type:
                args.update(kwargs)
            else:
                return {"error": "type of usage proxy not exist"}, 404

        #current_app.logger.debug(args)
        return return_proxy()


class ProxyList(Resource):

    def post(self, **kwargs):
        args = parser.parse(user_args, request)
        if 'type_usage' in kwargs:
            if kwargs['type_usage'] in list_type:
                args.update(kwargs)
            else:
                return {"error": "type of usage proxy not exist"}, 404
        # current_app.logger.debug(args)
        return return_proxy_list()

    def get(self, **kwargs):
        args = parser.parse(user_args, request)
        if 'type_usage' in kwargs:
            if kwargs['type_usage'] in list_type:
                args.update(kwargs)
            else:
                return {"error": "type of usage proxy not exist"}, 404
        # current_app.logger.debug(args)
        return return_proxy_list()

api = Api(proxy)
api.add_resource(Proxy, "/", endpoint="proxy")
api.add_resource(Proxy, "/<string:type_usage>", endpoint="proxy_by_type")

api = Api(proxy_list)
api.add_resource(ProxyList, "/", endpoint="proxy_list")
api.add_resource(ProxyList, "/<string:type_usage>", endpoint="proxy_list_by_type")