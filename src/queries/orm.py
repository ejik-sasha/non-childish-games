from sqlalchemy import text, insert, select, delete, update
from database import sync_engine, async_engine, session_factory, Base
from models import UsersOrm, CharactersOrm, CharacterClass


def create_tables():
    Base.metadata.drop_all(sync_engine)
    sync_engine.echo = True
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        user_sasha = UsersOrm(username="Sasha", email=None)
        session.add(user_sasha)
        session.commit()
        character_sasha = CharactersOrm(
            username="Sasha", 
            characterClass=CharacterClass.A, 
            characterId=user_sasha.id
            )
        session.add(character_sasha)
        session.commit()
