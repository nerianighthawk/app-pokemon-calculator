# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
from playhouse.postgres_ext import PostgresqlExtDatabase
import sys

sys.path.append('..')
import model.PokemonModel

api = Flask(__name__)


@api.route('/', methods=['GET'])
def hello():
    return 'hello:)'


@api.route('/getPokemon/<string:pokemonNo>', methods=['GET'])
def get_user(pokemonNo):
    try:
        pokemon = model.PokemonModel.Pokemon.get(model.PokemonModel.Pokemon.pokemonNo == pokemonNo)
    except model.PokemonModel.Pokemon.DoesNotExist:
        abort(404)

    result = {
        "result": True,
        "data": {
            "name": pokemon.pokemonName,
            "attack": pokemon.attack,
            "block": pokemon.block,
            "concentration": pokemon.concentration,
            "defense": pokemon.defense,
            "speed": pokemon.speed
        }
    }

    return make_response(jsonify(result))
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='127.0.0.1', port=3000)
