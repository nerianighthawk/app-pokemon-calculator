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
    pokemonNo = pe.TextField()
    pokemonName = pe.TextField()
    hitPoint = pe.IntegerField()
    attack = pe.IntegerField()
    block = pe.IntegerField()
    concentration = pe.IntegerField()
    defence = pe.IntegerField()
    speed = pe.IntegerField()
    weight = pe.IntegerField()
    CharacteristicId1 = pe.TextField()
    CharacteristicId2 = pe.TextField()
    CharacteristicId3 = pe.TextField()

    class Meta:
        database = db


# ポケモンテーブル作成
Pokemon.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("pokemon.tsv", "r"):
    (pokemonNo,
     pokemonName,
     hitPoint,
     attack,
     block,
     concentration,
     defence,
     speed,
     weight,
     CharacteristicId1,
     CharacteristicId2,
     CharacteristicId3) = tuple(line[:-1].split(" "))
    Pokemon.create(pokemonNo=pokemonNo,
                   pokemonName=pokemonName,
                   hitPoint=int(hitPoint),
                   attack=int(attack),
                   block=int(block),
                   concentration=int(concentration),
                   defence=int(defence),
                   speed=int(speed),
                   weight=int(weight),
                   CharacteristicId1=CharacteristicId1,
                   CharacteristicId2=CharacteristicId2,
                   CharacteristicId3=CharacteristicId3)
