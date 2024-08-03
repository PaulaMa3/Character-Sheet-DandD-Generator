from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tablas intermedias corregidas
language_character_association = Table('language_character_association', Base.metadata,
                                       Column('language_id', Integer, ForeignKey('languages.id')),
                                       Column('character_id', Integer, ForeignKey('characters.id')))

skill_character_association = Table('skill_character_association', Base.metadata,
                                    Column('skill_id', Integer, ForeignKey('skills.id')),
                                    Column('character_id', Integer, ForeignKey('characters.id')))

attribute_character_association = Table('attribute_character_association', Base.metadata,
                                        Column('attribute_id', Integer, ForeignKey('attributes.id')),
                                        Column('character_id', Integer, ForeignKey('characters.id')),
                                        Column('value', Integer))   # Añadir la columna 'value'

character_inventory_association = Table('character_inventory_association', Base.metadata,
                                        Column('character.id', Integer, ForeignKey('characters.id')),
                                        Column('inventory.id', Integer, ForeignKey('inventories.id')))

character_armor_association = Table('character_armor_association', Base.metadata,
                                    Column('character.id', Integer, ForeignKey('characters.id')),
                                    Column('armor.id', Integer, ForeignKey('armors.id')))

# Definición de la clase Character
class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    level = Column(Integer, nullable=False)
    image = ""
    race_id = Column(Integer, ForeignKey('races.id'))
    race = relationship('Race', back_populates='characters')
    class_id = Column(Integer, ForeignKey('classes.id'))
    c_class = relationship('Class', back_populates='characters')
    languages = relationship('Language', secondary=language_character_association, back_populates='characters')
    skills = relationship('Skill', secondary=skill_character_association, back_populates='characters')
    attributes = relationship('Attribute', secondary=attribute_character_association, back_populates='characters')
    armors = relationship('Armor', secondary=character_armor_association, back_populates='characters')
    inventories = relationship('Inventory', back_populates='character')  # Cambiar 'Inventories' a 'Inventory'

    def __init__(self, name, level, image, race_id, class_id):
        self.name = name
        self.level = level
        self.image = image
        self.race_id = race_id
        self.class_id = class_id

    def __repr__(self):
        return "Character {}: level {}".format(self.name, self.level)

    def __str__(self):
        return "Character {}: level {}".format(self.name, self.level)


# Tabla intermedia race_language_association corregida
race_language_association = Table('race_language_association', Base.metadata,
                                  Column('race_id', Integer, ForeignKey('races.id')),
                                  Column('language_id', Integer, ForeignKey('languages.id'))
                                  )


# Definición de la clase Race
class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    speed = Column(Integer, nullable=False)
    extra_strength = Column(Integer, nullable=False, default=0)
    extra_dexterity = Column(Integer, nullable=False, default=0)
    extra_constitution = Column(Integer, nullable=False, default=0)
    extra_intelligence = Column(Integer, nullable=False, default=0)
    extra_wisdom = Column(Integer, nullable=False, default=0)
    extra_charisma = Column(Integer, nullable=False, default=0)
    characters = relationship('Character', back_populates='race')  # Relación con Character
    languages = relationship('Language', secondary=race_language_association, back_populates='races')

    def __init__(self, name, speed, extra_strength=0, extra_dexterity=0, extra_constitution=0, extra_intelligence=0,
                 extra_wisdom=0, extra_charisma=0):
        self.name = name
        self.speed = speed
        self.extra_strength = extra_strength
        self.extra_dexterity = extra_dexterity
        self.extra_constitution = extra_constitution
        self.extra_intelligence = extra_intelligence
        self.extra_wisdom = extra_wisdom
        self.extra_charisma = extra_charisma

    def __repr__(self):
        return f"Raza {self.name}"


# Tablas intermedias para Class y Item
class_skill_association = Table('class_skill_association', Base.metadata,
                                Column('class_id', Integer, ForeignKey('classes.id')),
                                Column('skill_id', Integer, ForeignKey('skills.id'))
                                )

class_item_association = Table('class_item_association', Base.metadata,
                               Column('class_id', Integer, ForeignKey('classes.id')),
                               Column('item_id', Integer, ForeignKey('items.id'))
                               )
armor_class_association = Table('armor_class_association', Base.metadata,
                                Column('class_id', Integer, ForeignKey('classes.id')),
                                Column('armor_id', Integer, ForeignKey('armors.id')))

# Definición de la clase Class
class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hit_dice = Column(String(3), nullable=True)
    skills = relationship('Skill', secondary=class_skill_association, back_populates='classes')
    characters = relationship('Character', back_populates='c_class')
    items = relationship('Item', secondary=class_item_association, back_populates='classes')
    armors = relationship('Armor', secondary=armor_class_association, back_populates='classes', lazy='dynamic')  # Cambiar a 'dynamic'

    def __init__(self, name, hit_dice):
        self.name = name
        self.hit_dice = hit_dice

    def __repr__(self):
        return f"Clase {self.name}"

# Definición de la clase Skill
class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    classes = relationship('Class', secondary=class_skill_association, back_populates='skills')
    characters = relationship('Character', secondary=skill_character_association, back_populates='skills')
    attribute_id = Column(Integer, ForeignKey('attributes.id'))
    attribute = relationship('Attribute', back_populates='skills')

    def __init__(self, name, attribute_id):
        self.name = name
        self.attribute_id = attribute_id

    def __repr__(self):
        return f"Habilidad {self.name} de {self.attribute_id}"


# Definición de la clase Attribute
class Attribute(Base):
    __tablename__ = "attributes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    skills = relationship('Skill', back_populates='attribute')
    characters = relationship('Character', secondary=attribute_character_association, back_populates='attributes')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Atributo {self.name}"


# Definición de la clase Language
class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    races = relationship('Race', secondary=race_language_association, back_populates='languages')
    characters = relationship('Character', secondary=language_character_association, back_populates='languages')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Lenguaje {self.name}"


# Definición de la clase Category
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    items = relationship('Item', back_populates='category')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Categoría {self.name}"


# Tabla intermedia para Item y Inventory
item_inventory_association = Table('item_inventory_association', Base.metadata,
                                   Column('inventory_id', Integer, ForeignKey('inventories.id')),
                                   Column('item_id', Integer, ForeignKey('items.id')))


# Definición de la clase Inventory
class Inventory(Base):
    __tablename__ = "inventories"  # Asegúrate de que el nombre de la tabla sea coherente
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'))  # Agregar esta línea para definir la clave foránea
    character = relationship('Character', back_populates='inventories')  # Cambiar la relación para usar la clave foránea
    items = relationship('Item', secondary=item_inventory_association, back_populates='inventories')
    quantity = Column(Integer, nullable=False, default=1)

    def __init__(self, name, character_id, quantity):
        self.name = name
        self.character_id = character_id
        self.quantity = quantity

    def __repr__(self):
        return f"Este es el inventario de {self.character_id}"


# Definición de la clase Item
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='items')
    classes = relationship('Class', secondary=class_item_association, back_populates='items')
    inventories = relationship('Inventory', secondary=item_inventory_association, back_populates='items')

    def __init__(self, name, description, category_id):
        self.name = name
        self.description = description
        self.category_id = category_id

    def __repr__(self):
        return f"Objeto {self.name}: {self.description}"


class Armor(Base):
    __tablename__ = 'armors'  # Cambiar a plural

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Añadir el nombre de la armadura
    armor_class = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False)
    strength = Column(Integer, nullable=True)
    stealth = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    classes = relationship('Class', secondary=armor_class_association, back_populates='armors')
    characters = relationship('Character', secondary=character_armor_association, back_populates='armors')

    def __init__(self, name, armor_class, type, strength, stealth, weight):
        self.name = name  # Asegúrate de inicializar el nombre
        self.armor_class = armor_class
        self.type = type
        self.strength = strength
        self.stealth = stealth
        self.weight = weight

    def __repr__(self):
        return f"Armadura {self.name}. Clase de armadura: {self.armor_class}"

