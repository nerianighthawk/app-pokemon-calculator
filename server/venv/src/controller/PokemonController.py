# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, abort, make_response
from playhouse.postgres_ext import PostgresqlExtDatabase
import sys

sys.path.append('..')
from model.pokemon import Pokemon

pokemonApi = Blueprint('pokemon', __name__)


@pokemonApi.route('/getPokemon', methods=['GET'])
def get_pokemons():
    try:
        pokemonList = []
        for pokemon in Pokemon.select():
            pokemonList.append({"no": pokemon.no, "name": pokemon.name})
    except Pokemon.DoesNotExist:
        abort(404)

    result = {
        "result": True,
        "data": pokemonList
    }

    return make_response(jsonify(result))


@pokemonApi.route('/getPokemon/<string:pokemonNo>', methods=['GET'])
def get_pokemon(pokemonNo):
    try:
        pokemon = Pokemon.get(Pokemon.no == pokemonNo)
    except Pokemon.DoesNotExist:
        abort(404)

    result = {
        "result": True,
        "data": {
            "name": pokemon.name,
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
