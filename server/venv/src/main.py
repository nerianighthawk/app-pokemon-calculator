# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
from playhouse.postgres_ext import PostgresqlExtDatabase

from controller.pokemonController import pokemonApi

api = Flask(__name__)

api.register_blueprint(pokemonApi)


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='127.0.0.1', port=3000)
