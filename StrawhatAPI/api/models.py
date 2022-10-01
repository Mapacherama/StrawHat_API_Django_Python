from app import db
class OnePieceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    crew = db.Column(db.String(255))
    devilfruit = db.Column(db.String(255))
    residence = db.Column(db.String(255))
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

class Residence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255))
    kingdom = db.Column(db.String(255))
    type = db.Column(db.String(255))
    population = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "region": self.region,
            "kingdom": self.kingdom,
            "type": self.type,
            "population": self.population            
        }
