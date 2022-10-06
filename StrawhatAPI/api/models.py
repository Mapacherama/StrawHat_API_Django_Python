from app import db
from enum import Enum
from sqlalchemy import Integer, Enum, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import case

class OnePieceCharacter(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    bloodtype = db.Column(db.String(255))
    occupation = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    devilfruit = db.Column(db.String(255))
    isalive = db.Column(db.Boolean)
    hasdevilFruit = db.Column(db.Boolean)
    ispartOffleet = db.Column(db.Boolean)
    bounty = db.Column(db.Integer)
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    origin_id = db.Column(db.Integer, db.ForeignKey("Origin.id"))
    # crew_id = db.Column(db.Integer, db.ForeignKey("Crew.id"))
    # piratefleet_id = db.Column(db.Integer, db.ForeignKey("PirateFleet.id"))
    # devilfruit_id = db.Column(db.Integer, db.ForeignKey("DevilFruit.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bloodtype": self.bloodtype,
            "occupation": self.occupation,
            "nickname": self.nickname,
            "devilfruit": self.devilfruit,
            "isalive": self.isalive,
            "hasdevilfruit": self.hasdevilFruit,
            "ispartoffleet": self.ispartOffleet,
            "bounty": self.bounty,
            "age": self.age,
            "height": self.height,
            "birthday": self.birthday,
            "piratefleet": self.piratefleet,
            "bounty": self.bounty
        }
# Place of origin

class Origin(db.Model):
    __tablename__ = "Origin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    haskingdom = db.Column(Boolean, unique=False, default=True)
    characters = db.relationship("OnePieceCharacter", back_populates = "Origin")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "haskingdom": self.haskingdom
        }
#Crew

class Crew(db.Model):
    __tablename__ = "Crew"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    oceanOfOrigin = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    mainShip = db.Column(db.String(255))
    totalBounty = db.Column(db.Integer)
    # characters = db.relationship("OnePieceCharacter")

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
    __tablename__ = "PirateFleet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    totalPeople = db.Column(db.Integer)
    totalBounty = db.Column(db.Integer)

    # characters = db.relationship("OnePieceCharacter")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "captain": self.captain,
            "totalPeople": self.totalPeople,
            "totalBount": self.totalBounty
        }


#Devilfruit stuff

class DevilFruit(db.Model):
    __tablename__ = "DevilFruit"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    definition = db.Column(db.String(255))
    # parent = relationship("devilfruittype")


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

class DevilFruitTypes(db.Model):
    id = db.Column(Integer, primary_key=True)
    value = db.Column(Enum("paramecia", "zoan", "logia", name="ValueTypes"), default = "zoan")


