from sqlalchemy.orm import sessionmaker
from models import (Base, Character, Race, Class, Skill, Attribute, Language, Category, Item)
from db import engine, session, sessionmaker

def is_table_empty(session, model):
    return session.query(model).count() == 0

def populate_db():
    if is_table_empty(session, Attribute):
        attributes = [
            'Fuerza', 'Destreza', 'Constitución', 'Inteligencia', 'Sabiduría', 'Carisma'
        ]
        for attr in attributes:
            attribute = Attribute(name=attr)
            session.add(attribute)

    if is_table_empty(session, Skill):
        skills = [
            ('Acrobacias', 'Destreza'), ('Arcano', 'Inteligencia'), ('Atletismo', 'Fuerza'),
            ('Engaño', 'Carisma'), ('Historia', 'Inteligencia'), ('Interpretación', 'Carisma'),
            ('Investigación', 'Inteligencia'), ('Juego de Manos', 'Destreza'), ('Medicina', 'Sabiduría'),
            ('Naturaleza', 'Inteligencia'), ('Percepción', 'Sabiduría'), ('Perspicacia', 'Sabiduría'),
            ('Persuasión', 'Carisma'), ('Religión', 'Inteligencia'), ('Sigilo', 'Destreza'),
            ('Supervivencia', 'Sabiduría'), ('Trato con Animales', 'Sabiduría'), ('Intimidación', 'Carisma')
        ]
        for skill_name, attr_name in skills:
            attribute = session.query(Attribute).filter_by(name=attr_name).first()
            skill = Skill(name=skill_name, attribute_id=attribute.id)
            session.add(skill)

    if is_table_empty(session, Race):
        races = [
            ('Enano', 25, 2, 0, 2, 0, 0, 0, ['Comun', 'Enano']),
            ('Elfo', 30, 0, 2, 0, 0, 0, 0, ['Comun', 'Elfico']),
            ('Mediano', 25, 0, 2, 0, 0, 0, 0, ['Comun', 'Mediano']),
            ('Humano', 30, 1, 1, 1, 1, 1, 1, ['Comun'])
        ]
        for race_name, speed, str_bonus, dex_bonus, con_bonus, int_bonus, wis_bonus, cha_bonus, language_names in races:
            race = Race(name=race_name, speed=speed, extra_strength=str_bonus, extra_dexterity=dex_bonus,
                        extra_constitution=con_bonus, extra_intelligence=int_bonus, extra_wisdom=wis_bonus,
                        extra_charisma=cha_bonus)
            for language_name in language_names:
                language = session.query(Language).filter_by(name=language_name).first()
                if language:
                    race.languages.append(language)
            session.add(race)

    if is_table_empty(session, Class):
        classes = [
            ('Bárbaro', 'd12', 'Ninguna', 'Hachas, espadas, mazos', 'Ninguna'),
            ('Bardo', 'd8', 'Armaduras ligeras', 'Arcos, espadas cortas', 'Instrumentos musicales'),
            ('Clérigo', 'd8', 'Armaduras medias', 'Martillos, mazas', 'Kits de sanación'),
            ('Druida', 'd8', 'Armaduras ligeras', 'Báculos, hoces', 'Herboristería'),
            ('Guerrero', 'd10', 'Todas las armaduras', 'Todas las armas', 'Herramientas de artesano'),
            ('Monje', 'd8', 'Ninguna', 'Armas simples', 'Herramientas de artesano'),
            ('Paladín', 'd10', 'Todas las armaduras', 'Todas las armas', 'Herramientas de artesano'),
            ('Explorador', 'd10', 'Armaduras ligeras', 'Arcos, espadas cortas', 'Herramientas de ladrón'),
            ('Pícaro', 'd8', 'Armaduras ligeras', 'Armas simples', 'Herramientas de ladrón'),
            ('Hechicero', 'd6', 'Ninguna', 'Armas simples', 'Componentes mágicos'),
            ('Brujo', 'd8', 'Armaduras ligeras', 'Armas simples', 'Componentes mágicos'),
            ('Mago', 'd6', 'Ninguna', 'Armas simples', 'Componentes mágicos')
        ]
        for class_name, hit_dice, armor, weapons, tools in classes:
            class_ = Class(name=class_name, hit_dice=hit_dice, armor=armor, weapons=weapons, tools=tools)
            session.add(class_)

    if is_table_empty(session, Language):
        languages = ['Comun', 'Enano', 'Elfico', 'Mediano']
        for lang in languages:
            language = Language(name=lang)
            session.add(language)

    if is_table_empty(session, Category):
        categories = ['Arma', 'Herramienta', 'Armadura']
        for category_name in categories:
            category = Category(name=category_name)
            session.add(category)

    if is_table_empty(session, Item):
        items = [
            ('Espada corta', 'Arma básica para combate cuerpo a cuerpo', 'Arma'),
            ('Arco largo', 'Arma para combate a distancia', 'Arma'),
            ('Martillo de guerra', 'Arma poderosa para combate cuerpo a cuerpo', 'Arma'),
            ('Kit de sanación', 'Herramienta para sanar heridas', 'Herramienta'),
            ('Instrumento musical', 'Herramienta para bardos', 'Herramienta'),
            ('Armadura ligera', 'Protección básica', 'Armadura'),
            ('Armadura pesada', 'Protección avanzada', 'Armadura')
        ]
        for item_name, item_description, category_name in items:
            category = session.query(Category).filter_by(name=category_name).first()
            item = Item(name=item_name, description=item_description, category_id=category.id)
            session.add(item)

    session.commit()


