# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, abort, make_response
from playhouse.postgres_ext import PostgresqlExtDatabase
import sys

sys.path.append('..')
from model.pokemon import Pokemon

pokemonApi = Blueprint('pokemon', __name__)


@pokemonApi.route('/getPokemon/<string:pokemonNo>', methods=['GET'])
def get_user(pokemonNo):
    try:
        pokemon = Pokemon.get(Pokemon.pokemonNo == pokemonNo)
    except Pokemon.DoesNotExist:
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
