import os
from datetime import datetime
from urllib.parse import urlparse

from peewee import (
    CharField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
    IntegerField,
    Model,
    PostgresqlDatabase,
)

DATABASE_URL = os.getenv("DATABASE_URL")

url = urlparse(DATABASE_URL)

db_params = {
    "database": url.path[1:],  # Ignorar el primer "/" en la ruta
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port,
}
db = PostgresqlDatabase(**db_params)

class BaseModel(Model):
    class Meta:
        database = db

class Player(BaseModel):
    email = CharField(primary_key=True)
    name = CharField()
    last_name = CharField()
    password = CharField()

class VocabularyMatch(BaseModel):
    idMatch = IntegerField(primary_key=True)
    # Relacion de clave foránea con Player
    player = ForeignKeyField(Player, backref='vocabulary_matches', on_delete='CASCADE')
    num_words = IntegerField()
    difficulty = CharField()
    score = IntegerField()
    time = FloatField()
    date = DateTimeField(default=datetime.now)

class GrammarMatch(BaseModel):
    idMatch = IntegerField(primary_key=True)
    player = ForeignKeyField(Player, backref='grammar_matches', on_delete='CASCADE')
    session_name = CharField()
    difficulty = CharField()
    time = FloatField()
    score = IntegerField()
    completion = IntegerField()
    date = DateTimeField(default=datetime.now)


class ListeningMatch(BaseModel):
    idMatch = IntegerField(primary_key=True)
    player = ForeignKeyField(Player, backref='listening_matches', on_delete='CASCADE')
    score = IntegerField()
    accuracy = IntegerField()
    name_video = CharField()
    difficulty = CharField()
    time = IntegerField()
    date = DateTimeField(default=datetime.now)


db.connect()
db.create_tables([Player, VocabularyMatch, GrammarMatch, ListeningMatch])
