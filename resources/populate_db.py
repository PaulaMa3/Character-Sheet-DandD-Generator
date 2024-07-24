import os
import sys

# Agrega el path de Proyecto_Final al sys.path para poder importar db y models correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import sessionmaker
from models import Base, Attribute, Skill, Race, Class, Language, Category, Item
from db import engine

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

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

classes = [
    {"name": "Bárbaro", "hit_dice": "d12", "armor": "Armadura ligera, armadura media, escudos",
     "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Intimidación"],
     "items": ["Hacha de mano", "Gran hacha", "Paquete de aventurero"]},
    {"name": "Bardo", "hit_dice": "d8", "armor": "Armadura ligera",
     "weapons": "Armas simples, ballestas de mano, espadas largas, estoques, espadas cortas",
     "tools": "Tres instrumentos musicales a tu elección", "skills": ["Interpretación", "Engaño"],
     "items": ["Daga", "Ballesta de mano", "Paquete de músico"]},
    {"name": "Clérigo", "hit_dice": "d8", "armor": "Todas las armaduras, escudos", "weapons": "Armas simples",
     "tools": "Ninguno", "skills": ["Medicina", "Religión"], "items": ["Maza", "Escudo", "Paquete de sacerdote"]},
    {"name": "Druida", "hit_dice": "d8", "armor": "Armadura ligera, armadura media, escudos (no de metal)",
     "weapons": "Armas de palo, dardos, mazas, jabalinas, porras, hoces, hondas, lanzas", "tools": "Herbalismo",
     "skills": ["Naturaleza", "Medicina"], "items": ["Sickle", "Paquete de explorador"]},
    {"name": "Guerrero", "hit_dice": "d10", "armor": "Todas las armaduras, escudos",
     "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Supervivencia"],
     "items": ["Espada larga", "Escudo", "Paquete de aventurero"]},
    {"name": "Monje", "hit_dice": "d8", "armor": "Ninguno", "weapons": "Armas simples, espadas cortas",
     "tools": "Un tipo de herramienta de artesano o instrumento musical", "skills": ["Acrobacias", "Juego de Manos"],
     "items": ["Dardo", "Paquete de aventurero"]},
    {"name": "Paladín", "hit_dice": "d10", "armor": "Todas las armaduras, escudos",
     "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Atletismo", "Persuasión"],
     "items": ["Espada larga", "Escudo", "Paquete de sacerdote"]},
    {"name": "Explorador", "hit_dice": "d10", "armor": "Armadura ligera, armadura media, escudos",
     "weapons": "Armas simples, armas marciales", "tools": "Ninguno", "skills": ["Investigación", "Supervivencia"],
     "items": ["Arco largo", "Flechas", "Paquete de explorador"]},
    {"name": "Pícaro", "hit_dice": "d8", "armor": "Armadura ligera",
     "weapons": "Armas simples, ballestas de mano, espadas largas, estoques, espadas cortas",
     "tools": "Herramientas de ladrón", "skills": ["Sigilo", "Percepción"], "items": ["Daga", "Paquete de ladrón"]},
    {"name": "Hechicero", "hit_dice": "d6", "armor": "Ninguno",
     "weapons": "Dagas, dardos, hondas, bastones, ballestas ligeras", "tools": "Ninguno",
     "skills": ["Arcano", "Engaño"], "items": ["Bastón", "Paquete de explorador"]},
    {"name": "Brujo", "hit_dice": "d8", "armor": "Armadura ligera", "weapons": "Armas simples", "tools": "Ninguno",
     "skills": ["Arcano", "Engaño"], "items": ["Daga", "Libro de hechizos", "Paquete de erudito"]},
    {"name": "Mago", "hit_dice": "d6", "armor": "Ninguno",
     "weapons": "Dagas, dardos, hondas, bastones, ballestas ligeras", "tools": "Ninguno",
     "skills": ["Arcano", "Historia"], "items": ["Bastón", "Libro de hechizos", "Paquete de erudito"]}
]

categories = [
    {"name": "Arma"},
    {"name": "Herramienta"},
    {"name": "Armadura"}
]

items = [
    # Ítems para la clase Bárbaro
    {"name": "Hacha de mano", "description": "Una pequeña hacha de mano.", "category": "Arma"},
    {"name": "Gran hacha", "description": "Un hacha grande y pesada.", "category": "Arma"},
    {"name": "Jabalina", "description": "Un arma de asta para lanzar.", "category": "Arma"},
    {"name": "Paquete de aventurero", "description": "Un paquete con equipo básico para aventureros.",
     "category": "Herramienta"},

    # Ítems para la clase Bardo
    {"name": "Daga", "description": "Una pequeña arma corta.", "category": "Arma"},
    {"name": "Ballesta de mano", "description": "Una pequeña ballesta que se puede usar con una mano.",
     "category": "Arma"},
    {"name": "Espada larga", "description": "Una espada versátil.", "category": "Arma"},
    {"name": "Estoque", "description": "Un arma de filo delgada y puntiaguda.", "category": "Arma"},
    {"name": "Paquete de diplomático", "description": "Un paquete con equipo para diplomáticos.",
     "category": "Herramienta"},
    {"name": "Paquete de músico", "description": "Un paquete con instrumentos musicales.", "category": "Herramienta"},
    {"name": "Armadura de cuero", "description": "Armadura ligera hecha de cuero.", "category": "Armadura"},

    # Ítems básicos para otras clases
    {"name": "Espada corta", "description": "Una espada más corta y ligera.", "category": "Arma"},
    {"name": "Martillo de guerra", "description": "Un pesado martillo usado en combate.", "category": "Arma"},
    {"name": "Escudo", "description": "Una pieza de armadura para protegerse.", "category": "Armadura"},
    {"name": "Armadura de malla", "description": "Armadura hecha de anillos de metal entrelazados.",
     "category": "Armadura"},
    {"name": "Arco largo", "description": "Un arco grande para disparar a largas distancias.", "category": "Arma"},
    {"name": "Flechas", "description": "Munición para arco.", "category": "Arma"},
    {"name": "Mochila de explorador", "description": "Un paquete con equipo para explorar.", "category": "Herramienta"},
    {"name": "Herramientas de ladrón", "description": "Conjunto de herramientas para abrir cerraduras.",
     "category": "Herramienta"},
    {"name": "Instrumento musical", "description": "Instrumento usado por bardos y otros músicos.",
     "category": "Herramienta"},
    {"name": "Antorcha", "description": "Una antorcha para iluminar el camino.", "category": "Herramienta"},
    {"name": "Raciones de comida", "description": "Raciones secas para varios días.", "category": "Herramienta"},
    {"name": "Cantimplora", "description": "Un recipiente para llevar agua.", "category": "Herramienta"},
    {"name": "Soga", "description": "Un trozo de cuerda útil en muchas situaciones.", "category": "Herramienta"}
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


# Función para comprobar si una tabla está vacía
def is_table_empty(session, model):
    return session.query(model).count() == 0


# Poblar la base de datos si las tablas están vacías
def populate_db():
    if is_table_empty(session, Attribute):
        for attribute_data in attributes:
            attribute = Attribute(name=attribute_data["name"])
            session.add(attribute)

    if is_table_empty(session, Skill):
        for skill_data in skills:
            attribute = session.query(Attribute).filter_by(name=skill_data["attribute"]).first()
            skill = Skill(name=skill_data["name"], attribute_id=attribute.id)
            session.add(skill)

    if is_table_empty(session, Language):
        for language_data in languages:
            language = Language(name=language_data["name"])
            session.add(language)

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

    if is_table_empty(session, Category):
        for category_data in categories:
            category = Category(name=category_data["name"])
            session.add(category)

    if is_table_empty(session, Item):
        for item_data in items:
            category = session.query(Category).filter_by(name=item_data["category"]).first()
            item = Item(
                name=item_data["name"],
                description=item_data["description"],
                category_id=category.id
            )
            session.add(item)

    if is_table_empty(session, Class):
        for class_data in classes:
            class_ = Class(
                name=class_data["name"],
                hit_dice=class_data["hit_dice"],
                armor=class_data["armor"],
                weapons=class_data["weapons"],
                tools=class_data["tools"]
            )
            session.add(class_)
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
            session.add(class_)

    session.commit()


if __name__ == "__main__":
    populate_db()
