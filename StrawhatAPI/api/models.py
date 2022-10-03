from app import db
from enum import Enum
from sqlalchemy import Integer, Enum
#https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one
class OnePieceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    bloodType = db.Column(db.String(255))
    occupation = db.Column(db.String(255))
    nickName = db.Column(db.String(255))

    devilfruit = db.Column(db.String(255))
    origin = db.Column(db.String(255), db.ForeignKey('origin.id'))
    crew = db.Column(db.String(255), db.ForeignKey('crew.id'))
    piratefleet = db.Column(db.String(255), db.ForeignKey('crew.id'))
    bounty = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "devilfruit": self.devilfruit,
            "residence": self.residence,
            "bounty": self.bounty
        }
# Place of origin
class Origin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hasKingdom = db.Column(Boolean, unique=False, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "haskingdom": self.hasKingdom
        }

#Crew
class Crew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    oceanOfOrigin = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    mainShip = db.Column(db.String(255))
    totalBounty = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "oceanoforigin": self.oceanOfOrigin,
            "captain": self.captain,
            "mainship": self.mainShip,
            "totalBount": self.totalBounty
        }

#Piratefleet
class PirateFleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    totalBounty = db.Column(db.Integer)
    totalBounty = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "oceanoforigin": self.oceanOfOrigin,
            "captain": self.captain,
            "mainship": self.mainShip,
            "totalBount": self.totalBounty
        }


#Devilfruit stuff
class DevilFruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    definition = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "region": self.region,
            "kingdom": self.kingdom,
            "type": self.type,
            "population": self.population
        }

class DevilFruitTypes(Enum):
        PARAMECIA = 1
        ZOAN = 2
        LOGIA = 3

class DevilFruitTypes(Base):
    __devilfruittype__ = 'devilfruittype'
    id = Column(Integer, primary_key=True)
    value = Column(Enum(DevilFruitTypes))

