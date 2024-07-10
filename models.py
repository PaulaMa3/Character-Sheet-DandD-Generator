from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Character (Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    c_class = Column(String(20), nullable=False)
    race = Column(String(20), nullable=False)
    level = Column(Integer, nullable=True)

    def __init__(self, name, race, c_class, level):
        self.name = name
        self.c_class = c_class
        self.race = race
        self.level = level

    def __repr__(self):
        return "Character {}: {}, {} level {}" .format(self.name, self.race, self.c_class, self.level)

    def __str__(self):
        return "Character {}: {}, {} level {}".format(self.name, self.race, self.c_class, self.level)
