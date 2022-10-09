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
    origin_id = Column(Integer, ForeignKey("origin.id", ondelete="CASCADE"))


# Place of origin

class origin(BaseMixin):
    __tablename__ = "origin"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hasKingdom = Column(Boolean, unique=False, default=True)







