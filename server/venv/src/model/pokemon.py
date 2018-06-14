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
    no = pe.TextField(primary_key=True)
    name = pe.TextField()
    hitPoint = pe.IntegerField()
    attack = pe.IntegerField()
    block = pe.IntegerField()
    concentration = pe.IntegerField()
    defense = pe.IntegerField()
    speed = pe.IntegerField()
    weight = pe.IntegerField()

    class Meta:
        database = db


# ポケモンテーブル作成
Pokemon.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("resources/pokemon.tsv", "r"):
    (no,
     name,
     hitPoint,
     attack,
     block,
     concentration,
     defense,
     speed,
     weight) = tuple(line[:-1].split("\u0009"))
    Pokemon.create(no=no,
                   name=name,
                   hitPoint=int(hitPoint),
                   attack=int(attack),
                   block=int(block),
                   concentration=int(concentration),
                   defense=int(defense),
                   speed=int(speed),
                   weight=int(weight))
