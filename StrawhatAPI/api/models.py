from app import db


class OnePieceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    crew = db.Column(db.String)
    devilfruit = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "devilfruit": self.devilfruit
        }