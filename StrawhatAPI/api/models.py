from api import db

import enum

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Enum

class BaseMixin(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class OnePieceCharacter(BaseMixin):
    __tablename__ = "character"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255))
    bloodtype = Column(db.String(255))
    occupation = Column(String(255))
    nickname = Column(String(255))
    devilfruit = Column(String(255))
    isalive = Column(Boolean)
    hasdevilFruit = Column(Boolean)
    ispartOffleet = Column(Boolean)
    bounty = Column(Integer)
    age = Column(Integer)
    height = Column(Integer)
    birthday = Column(Date)
    origin_id = Column(Integer, ForeignKey("origin.id", ondelete="CASCADE"))
    crew_id = Column(Integer, ForeignKey("crew.id", ondelete="CASCADE"))
    piratefleet_id = Column(Integer, ForeignKey("piratefleet.id", ondelete="CASCADE"))
    devilfruit_id = Column(Integer, ForeignKey("devilfruit.id", ondelete="CASCADE"))


# Place of origin

class origin(BaseMixin):
    __tablename__ = "origin"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hasKingdom = Column(Boolean, unique=False, default=True)
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"))

class crew(BaseMixin):
    __tablename__ = "crew"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    oceanoforigin = Column(String(255))
    captain = Column(String(255))
    mainship = Column(String(255))
    totalbounty = Column(Integer)
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"))


class piratefleet(BaseMixin):
    __tablename__ = "piratefleet"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    captain = Column(String(255))
    totalpeople = Column(Integer)
    totalbounty = Column(Integer)
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"))

class devilfruittype(enum.Enum):
    paramecia = 1
    zoan = 2
    logia = 3

class devilfruit(BaseMixin):
    __tablename__ = "devilfruit"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    meaning = Column(String(255))
    typeofdevilfruit = Column(Enum(devilfruittype))
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"))








