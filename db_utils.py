from sqlalchemy.orm import sessionmaker
from models import Race, Class
from db import engine

def get_races():
    Session = sessionmaker(bind=engine)
    session = Session()
    races = session.query(Race).all()
    session.close()
    return [race.name for race in races]

def get_classes():
    Session = sessionmaker(bind=engine)
    session = Session()
    classes = session.query(Class).all()
    session.close()
    return [c_class.name for c_class in classes]


