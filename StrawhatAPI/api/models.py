from api import db

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

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
    __tablename__ = "characters"

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

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "bloodtype": self.bloodtype,
    #         "occupation": self.occupation,
    #         "nickname": self.nickname,
    #         "devilfruit": self.devilfruit,
    #         "isalive": self.isalive,
    #         "hasdevilfruit": self.hasdevilFruit,
    #         "ispartoffleet": self.ispartOffleet,
    #         "bounty": self.bounty,
    #         "age": self.age,
    #         "height": self.height,
    #         "birthday": self.birthday,
    #         "piratefleet": self.piratefleet,
    #         "bounty": self.bounty
    #     }
# Place of origin

class Origin(BaseMixin):
    __tablename__ = "origin"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255))
    haskingdom = Column(Boolean, unique=False, default=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "haskingdom": self.haskingdom
    #     }



