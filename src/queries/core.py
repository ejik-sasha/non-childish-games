from sqlalchemy import text, insert, select, delete, update
from database import sync_engine, async_engine, session
from models import metadata_obj, UsersOrm

def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def get_v():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")
    
async def get_123456():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.all()=}")
def insert_data():
    with sync_engine.connect() as conn:
        #stmt = """INSERT INTO users (username) VALUES
        #('Sasha'),
        #('Masha');"""
        stmt = insert(users_table).values(
            [
                {"username": "Sasha"},
                {"username": "Masha"},
            ]
        )
        conn.execute(stmt)
        conn.commit()