from app import db
from enum import Enum
from sqlalchemy import Integer, Enum, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import case
#https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one

# class Parent(Base):
#     __tablename__ = "parent"
#     id = Column(Integer, primary_key=True)
#
#     # one-to-many collection
#     children = relationship("Child", back_populates="parent")
#
#
# class Child(Base):
#     __tablename__ = "child"
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey("parent.id"))
#
#     # many-to-one scalar
#     parent = relationship("Parent", back_populates="children")
class OnePieceCharacter(db.Model):
    __table_args__ = {'extend_existing': True}
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
    # Relationships (?)
    originRelationship = relationship("Origin", back_populates="OnePieceCharacter")
    crewRelationship = relationship("Crew", back_populates="OnePieceCharacter")
    piratefleetRelationship = relationship("PirateFleet", back_populates="OnePieceCharacter")
    DevilFruitRelationship = relationship("DevilFruit", back_populates="OnePieceCharacter")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bloodtype": self.bloodType,
            "occupation": self.occupation,
            "nickName": self.nickName,
            "devilfruit": self.devilfruit,
            "origin": self.origin,
            "crew": self.crew,
            "piratefleet": self.piratefleet,
            "bounty": self.bounty
        }
# Place of origin

class Origin(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hasKingdom = db.Column(Boolean, unique=False, default=True)
    parent = relationship("OnePieceCharacter", back_populates="Origin")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "haskingdom": self.hasKingdom
        }

#Crew

class Crew(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    oceanOfOrigin = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    mainShip = db.Column(db.String(255))
    totalBounty = db.Column(db.Integer)
    parent = relationship("OnePieceCharacter", back_populates="Crew")

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
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    captain = db.Column(db.String(255))
    totalPeople = db.Column(db.Integer)
    totalBounty = db.Column(db.Integer)
    parent = relationship("OnePieceCharacter", back_populates="Origin")

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
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    definition = db.Column(db.String(255))
    parent = relationship("devilfruittype", back_populates="DevilFruit")


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
    __devilfruittype__ = 'devilfruittype'
    id = db.Column(Integer, primary_key=True)
    value = db.Column(Enum("paramecia", "zoan", "logia", name="ValueTypes"), default = "zoan")
    originRelationship = relationship("DevilFruit", back_populates="devilfruittype")

