from app import db
class OnePieceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    crew = db.Column(db.String(255))
    devilfruit = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "devilfruit": self.devilfruit
        }