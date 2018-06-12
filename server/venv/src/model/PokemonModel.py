# -*- coding: utf-8 -*-
import peewee as pe
from playhouse.postgres_ext import PostgresqlExtDatabase

# データベース指定
db = PostgresqlExtDatabase(
    database='pokemon',
    user='postgres',
    password="postgres",
    host="127.0.0.1",
    port=5432,
    register_hstore=False)


# ポケモンモデルを定義
class Pokemon(pe.Model):
    pokemonNo = pe.TextField(primary_key=True)
    pokemonName = pe.TextField()
    hitPoint = pe.IntegerField()
    attack = pe.IntegerField()
    block = pe.IntegerField()
    concentration = pe.IntegerField()
    defense = pe.IntegerField()
    speed = pe.IntegerField()
    weight = pe.IntegerField()

    class Meta:
        database = db
