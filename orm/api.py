from engine import engine
from sqlalchemy.orm import Session
from orm.classes.Client import Client
from orm.classes.Accountant import Accountant


async def create_accountant(tg_id: int, username: str):
    session = Session(engine)
    try:
        acc = Accountant(
            tgAccId=tg_id,
            username=username,
        )
        session.add(acc)
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False


async def create_client(tg_id: int, username: str):
    session = Session(engine)
    try:
        client = Client(
            tgClientId=tg_id,
            username=username,
        )
        session.add(client)
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False
