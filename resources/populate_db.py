from db import session
from models import *


# Datos para poblar las tablas
attributes = [
    {"name": "Fuerza"},
    {"name": "Destreza"},
    {"name": "Constitución"},
    {"name": "Inteligencia"},
    {"name": "Sabiduría"},
    {"name": "Carisma"}
]

skills = [
    {"name": "Acrobacias", "attribute": "Destreza"},
    {"name": "Manejo de Animales", "attribute": "Sabiduría"},
    {"name": "Arcano", "attribute": "Inteligencia"},
    {"name": "Atletismo", "attribute": "Fuerza"},
    {"name": "Engaño", "attribute": "Carisma"},
    {"name": "Historia", "attribute": "Inteligencia"},
    {"name": "Perspicacia", "attribute": "Sabiduría"},
    {"name": "Intimidación", "attribute": "Carisma"},
    {"name": "Investigación", "attribute": "Inteligencia"},
    {"name": "Medicina", "attribute": "Sabiduría"},
    {"name": "Naturaleza", "attribute": "Inteligencia"},
    {"name": "Percepción", "attribute": "Sabiduría"},
    {"name": "Interpretación", "attribute": "Carisma"},
    {"name": "Persuasión", "attribute": "Carisma"},
    {"name": "Religión", "attribute": "Inteligencia"},
    {"name": "Juego de Manos", "attribute": "Destreza"},
    {"name": "Sigilo", "attribute": "Destreza"},
    {"name": "Supervivencia", "attribute": "Sabiduría"}
]

races = [
    {"name": "Humano", "speed": 30, "extra_strength": 1, "extra_dexterity": 1, "extra_constitution": 1,
     "extra_intelligence": 1, "extra_wisdom": 1, "extra_charisma": 1, "languages": ["Común"], "subraces": []},
    {"name": "Elfo", "speed": 30, "extra_dexterity": 2, "extra_strength": 0, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Élfico"], "subraces": [
        {"name": "Elfo Alto", "extra_intelligence": 1},
        {"name": "Elfo Silvano", "extra_wisdom": 1},
        {"name": "Drow", "extra_charisma": 1}
    ]},
    {"name": "Enano", "speed": 25, "extra_strength": 0, "extra_dexterity": 0, "extra_constitution": 2,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Enano"], "subraces": [
        {"name": "Enano de Colinas", "extra_wisdom": 1},
        {"name": "Enano de Montañas", "extra_strength": 2}
    ]},
    {"name": "Mediano", "speed": 25, "extra_strength": 0, "extra_dexterity": 2, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Mediano"], "subraces": [
        {"name": "Mediano Piesligeros", "extra_charisma": 1},
        {"name": "Mediano Recio", "extra_constitution": 1}
    ]},
    {"name": "Gnomo", "speed": 25, "extra_strength": 0, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 2, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Gnomo"], "subraces": [
        {"name": "Gnomo de Bosque", "extra_dexterity": 1},
        {"name": "Gnomo de Roca", "extra_constitution": 1}
    ]},
    {"name": "Semielfo", "speed": 30, "extra_strength": 0, "extra_dexterity": 2, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 1, "languages": ["Común", "Élfico"], "subraces": []},
    {"name": "Semiorco", "speed": 30, "extra_strength": 2, "extra_dexterity": 0, "extra_constitution": 1,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Orco"], "subraces": []},
    {"name": "Tiefling", "speed": 30, "extra_strength": 0, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 1, "extra_wisdom": 0, "extra_charisma": 2, "languages": ["Común", "Infernal"],
     "subraces": []},
    {"name": "Aasimar", "speed": 30, "extra_strength": 0, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 1, "extra_charisma": 2, "languages": ["Común", "Celestial"],
     "subraces": []},
    {"name": "Genasi", "speed": 30, "extra_strength": 0, "extra_dexterity": 0, "extra_constitution": 2,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Primordial"],
     "subraces": [
         {"name": "Genasi del Aire", "extra_dexterity": 1},
         {"name": "Genasi de Fuego", "extra_intelligence": 1},
         {"name": "Genasi de Tierra", "extra_strength": 1},
         {"name": "Genasi de Agua", "extra_wisdom": 1}
     ]},
    {"name": "Goliat", "speed": 30, "extra_strength": 2, "extra_dexterity": 0, "extra_constitution": 1,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": 0, "languages": ["Común", "Gigante"],
     "subraces": []},
    {"name": "Kobold", "speed": 30, "extra_strength": -2, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 0, "extra_charisma": -2, "languages": ["Común", "Dracónico"],
     "subraces": []},
    {"name": "Firbolg", "speed": 30, "extra_strength": 1, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 2, "extra_charisma": 0, "languages": ["Común", "Gigante"],
     "subraces": []},
    {"name": "Kenku", "speed": 30, "extra_strength": 0, "extra_dexterity": 2, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 1, "extra_charisma": 0, "languages": ["Común", "Auran"], "subraces": []},
    {"name": "Tortle", "speed": 30, "extra_strength": 2, "extra_dexterity": 0, "extra_constitution": 0,
     "extra_intelligence": 0, "extra_wisdom": 1, "extra_charisma": 0, "languages": ["Común", "Aquan"], "subraces": []}
]

languages = [
    {"name": "Común"},
    {"name": "Élfico"},
    {"name": "Enano"},
    {"name": "Mediano"},
    {"name": "Gnomo"},
    {"name": "Orco"},
    {"name": "Infernal"},
    {"name": "Celestial"},
    {"name": "Primordial"},
    {"name": "Gigante"},
    {"name": "Dracónico"},
    {"name": "Aquan"},
    {"name": "Auran"}
]

classes = [
    {"name": "Bárbaro", "hit_dice": "d12", "armor": ["Pesada"], "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Intimidación"], "items": ["Hacha de mano", "Gran hacha", "Paquete de aventurero"]},
    {"name": "Bardo", "hit_dice": "d8", "armor": ["Ligera"], "weapons": "Armas simples, ballestas de mano, espadas largas, estoques, espadas cortas", "tools": "Tres instrumentos musicales a tu elección", "skills": ["Interpretación", "Engaño"], "items": ["Daga", "Ballesta de mano", "Paquete de músico"]},
    {"name": "Clérigo", "hit_dice": "d8", "armor": ["Pesada"], "weapons": "Armas simples", "tools": "Ninguno", "skills": ["Medicina", "Religión"], "items": ["Maza", "Escudo", "Paquete de sacerdote"]},
    {"name": "Druida", "hit_dice": "d8", "armor": ["Ligera", "Media"], "weapons": "Armas de palo, dardos, mazas, jabalinas, porras, hoces, hondas, lanzas", "tools": "Herbalismo", "skills": ["Naturaleza", "Medicina"], "items": ["Sickle", "Paquete de explorador"]},
    {"name": "Guerrero", "hit_dice": "d10", "armor": ["Ligera", "Media", "Pesada"], "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Supervivencia"], "items": ["Espada larga", "Escudo", "Paquete de aventurero"]},
    {"name": "Monje", "hit_dice": "d8", "armor": [], "weapons": "Armas simples, espadas cortas", "tools": "Un tipo de herramienta de artesano o instrumento musical", "skills": ["Acrobacias", "Juego de Manos"], "items": ["Dardo", "Paquete de aventurero"]},
    {"name": "Paladín", "hit_dice": "d10", "armor": ["Pesada"], "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Persuasión"], "items": ["Espada larga", "Escudo", "Paquete de sacerdote"]},
    {"name": "Explorador", "hit_dice": "d10", "armor": ["Ligera", "Media"], "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Investigación", "Supervivencia"], "items": ["Arco largo", "Flechas", "Paquete de explorador"]},
    {"name": "Pícaro", "hit_dice": "d8", "armor": ["Ligera"], "weapons": "Armas simples, ballestas de mano, espadas largas, estoques, espadas cortas", "tools": "Herramientas de ladrón", "skills": ["Sigilo", "Percepción"], "items": ["Daga", "Paquete de ladrón"]},
    {"name": "Hechicero", "hit_dice": "d6", "armor": [], "weapons": "Dagas, dardos, hondas, bastones, ballestas ligeras", "tools": "Ninguno", "skills": ["Arcano", "Engaño"], "items": ["Bastón", "Paquete de explorador"]},
    {"name": "Brujo", "hit_dice": "d8", "armor": ["Ligera"], "weapons": "Armas simples", "tools": "Ninguno", "skills": ["Arcano", "Engaño"], "items": ["Daga", "Libro de hechizos", "Paquete de erudito"]},
    {"name": "Mago", "hit_dice": "d6", "armor": [], "weapons": "Dagas, dardos, hondas, bastones, ballestas ligeras", "tools": "Ninguno", "skills": ["Arcano", "Historia"], "items": ["Bastón", "Libro de hechizos", "Paquete de erudito"]}
]

categories = [
    {"name": "Arma"},
    {"name": "Herramienta"},
    {"name": "Armas Simples"},
    {"name": "Armas Marciales"},
    {"name": "Herramientas de Ladrón"},
    {"name": "Instrumentos Musicales"},
    {"name": "Paquetes"},
    {"name": "Libros"},
    {"name": "Bastones"}
]

items = [
    {"name": "Hacha de mano", "description": "Una pequeña hacha de mano.", "category": "Armas Simples"},
    {"name": "Gran hacha", "description": "Un hacha grande y pesada.", "category": "Armas Marciales"},
    {"name": "Jabalina", "description": "Un arma de asta para lanzar.", "category": "Armas Simples"},
    {"name": "Paquete de aventurero", "description": "Un paquete con equipo básico para aventureros.", "category": "Paquetes"},
    {"name": "Daga", "description": "Una pequeña arma corta.", "category": "Armas Simples"},
    {"name": "Ballesta de mano", "description": "Una pequeña ballesta que se puede usar con una mano.", "category": "Armas Simples"},
    {"name": "Espada larga", "description": "Una espada versátil.", "category": "Armas Marciales"},
    {"name": "Estoque", "description": "Un arma de filo delgada y puntiaguda.", "category": "Armas Marciales"},
    {"name": "Paquete de diplomático", "description": "Un paquete con equipo para diplomáticos.", "category": "Paquetes"},
    {"name": "Paquete de músico", "description": "Un paquete con instrumentos musicales.", "category": "Paquetes"},
    {"name": "Espada corta", "description": "Una espada más corta y ligera.", "category": "Armas Marciales"},
    {"name": "Martillo de guerra", "description": "Un pesado martillo usado en combate.", "category": "Armas Marciales"},
    {"name": "Arco largo", "description": "Un arco grande para disparar a largas distancias.", "category": "Armas Marciales"},
    {"name": "Flechas", "description": "Munición para arco.", "category": "Armas Marciales"},
    {"name": "Mochila de explorador", "description": "Un paquete con equipo para explorar.", "category": "Paquetes"},
    {"name": "Herramientas de ladrón", "description": "Conjunto de herramientas para abrir cerraduras.", "category": "Herramientas de Ladrón"},
    {"name": "Instrumento musical", "description": "Instrumento usado por bardos y otros músicos.", "category": "Instrumentos Musicales"},
    {"name": "Antorcha", "description": "Una antorcha para iluminar el camino.", "category": "Herramienta"},
    {"name": "Raciones de comida", "description": "Raciones secas para varios días.", "category": "Herramienta"},
    {"name": "Cantimplora", "description": "Un recipiente para llevar agua.", "category": "Herramienta"},
    {"name": "Soga", "description": "Un trozo de cuerda útil en muchas situaciones.", "category": "Herramienta"}
]

armors = [
    {"name": "Armadura de cuero", "armor_class": 11, "type": "Ligera", "strength": 0, "stealth": 0, "weight": 10.0},
    {"name": "Armadura acolchada", "armor_class": 11, "type": "Ligera", "strength": 0, "stealth": -1, "weight": 8.0},
    {"name": "Armadura de cuero tachonado", "armor_class": 12, "type": "Ligera", "strength": 0, "stealth": -1, "weight": 13.0},
    {"name": "Armadura de malla", "armor_class": 14, "type": "Media", "strength": 0, "stealth": -1, "weight": 40.0},
    {"name": "Armadura de escamas", "armor_class": 14, "type": "Media", "strength": 0, "stealth": -1, "weight": 45.0},
    {"name": "Armadura de media placa", "armor_class": 15, "type": "Media", "strength": 0, "stealth": -1, "weight": 50.0},
    {"name": "Armadura de piel", "armor_class": 11, "type": "Ligera", "strength": 0, "stealth": 1, "weight": 12.0},
    {"name": "Armadura de placas", "armor_class": 18, "type": "Pesada", "strength": 15, "stealth": -1, "weight": 65.0},
    {"name": "Armadura de anillas", "armor_class": 14, "type": "Media", "strength": 0, "stealth": -1, "weight": 55.0},
    {"name": "Cota de mallas", "armor_class": 16, "type": "Media", "strength": 13, "stealth": -1, "weight": 40.0},
    {"name": "Cota de escamas", "armor_class": 14, "type": "Media", "strength": 0, "stealth": -1, "weight": 45.0},
    {"name": "Armadura de cuero endurecido", "armor_class": 12, "type": "Ligera", "strength": 0, "stealth": 1, "weight": 14.0},
    {"name": "Armadura de anillas", "armor_class": 15, "type": "Media", "strength": 13, "stealth": -1, "weight": 60.0},
    {"name": "Armadura de peto", "armor_class": 14, "type": "Media", "strength": 0, "stealth": 1, "weight": 20.0},
    {"name": "Armadura de campo", "armor_class": 16, "type": "Pesada", "strength": 15, "stealth": -1, "weight": 70.0},
    {"name": "Armadura de cuero reforzado", "armor_class": 13, "type": "Ligera", "strength": 0, "stealth": 1, "weight": 15.0}
]

# Función para comprobar si una tabla está vacía
def is_table_empty(session, model):
    return session.query(model).count() == 0

# Poblar la base de datos si las tablas están vacías
def populate_db():
    global armors
    global attributes
    global skills
    global items
    global categories
    global languages
    global races
    global classes

    if is_table_empty(session, Attribute):
        for attribute_data in attributes:
            attribute = Attribute(name=attribute_data["name"])
            session.add(attribute)
        session.commit()

    if is_table_empty(session, Class):
        for class_data in classes:
            class_ = Class(
                name=class_data["name"],
                hit_dice=class_data["hit_dice"])
            session.add(class_)
        session.commit()

    if is_table_empty(session, Skill):
        for skill_data in skills:
            attribute = session.query(Attribute).filter_by(name=skill_data["attribute"]).first()
            skill = Skill(name=skill_data["name"], attribute_id=attribute.id)
            session.add(skill)
        session.commit()

    if is_table_empty(session, Language):
        for language_data in languages:
            language = Language(name=language_data["name"])
            session.add(language)
        session.commit()

    if is_table_empty(session, Race):
        for race_data in races:
            race = Race(
                name=race_data["name"],
                speed=race_data["speed"],
                extra_strength=race_data["extra_strength"],
                extra_dexterity=race_data["extra_dexterity"],
                extra_constitution=race_data["extra_constitution"],
                extra_intelligence=race_data["extra_intelligence"],
                extra_wisdom=race_data["extra_wisdom"],
                extra_charisma=race_data["extra_charisma"]
            )
            session.add(race)
        session.commit()

        for race_data in races:
            race = session.query(Race).filter_by(name=race_data["name"]).first()
            for language_name in race_data["languages"]:
                language = session.query(Language).filter_by(name=language_name).first()
                if language:
                    race.languages.append(language)
            session.add(race)
        session.commit()

    if is_table_empty(session, Category):
        for category_data in categories:
            category = Category(name=category_data["name"])
            session.add(category)
        session.commit()

    if is_table_empty(session, Item):
        for item_data in items:
            category = session.query(Category).filter_by(name=item_data["category"]).first()
            item = Item(
                name=item_data["name"],
                description=item_data["description"],
                category_id=category.id
            )
            session.add(item)
        session.commit()

    if is_table_empty(session, Armor):
        for armor_data in armors:
            armor = Armor(
                name=armor_data["name"],
                armor_class=armor_data["armor_class"],
                type=armor_data["type"],
                strength=armor_data.get("strength"),
                stealth=armor_data.get("stealth"),
                weight=armor_data.get("weight")
            )
            session.add(armor)
        session.commit()

    for class_data in classes:
        class_ = session.query(Class).filter_by(name=class_data["name"]).first()
        for skill_name in class_data["skills"]:
            skill = session.query(Skill).filter_by(name=skill_name).first()
            if skill:
                class_.skills.append(skill)
        for item_name in class_data["items"]:
            item = session.query(Item).filter_by(name=item_name).first()
            if item:
                class_.items.append(item)
        for armor_type in class_data["armor"]:
            if armor_type == "Todas las armaduras":
                armors = session.query(Armor).all()
            else:
                armors = session.query(Armor).filter_by(type=armor_type).all()
            for armor in armors:
                class_.armors.append(armor)
        session.add(class_)
    session.commit()

if __name__ == "__main__":
    populate_db()
