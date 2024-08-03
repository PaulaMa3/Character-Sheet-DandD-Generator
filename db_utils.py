from sqlalchemy.orm import sessionmaker
from models import Race, Class
from db import engine

def get_races():
    Session = sessionmaker(bind=engine)
    session = Session()
    races = session.query(Race).all()
    session.close()
    return {
        race.name: {
            'Fuerza': race.extra_strength,
            'Destreza': race.extra_dexterity,
            'Constitución': race.extra_constitution,
            'Inteligencia': race.extra_intelligence,
            'Sabiduría': race.extra_wisdom,
            'Carisma': race.extra_charisma,
        }
        for race in races
    }

def get_classes():
    Session = sessionmaker(bind=engine)
    session = Session()
    classes = session.query(Class).all()
    session.close()
    return [c_class.name for c_class in classes]

def get_class_armor(class_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    class_obj = session.query(Class).filter_by(name=class_name).first()
    if class_obj and class_obj.armors.count() > 0:  # Verifica si hay armaduras asignadas
        armor_name = class_obj.armors[0].name
    else:
        armor_name = "Sin armadura"  # Maneja el caso donde no hay armaduras asignadas
    return armor_name

