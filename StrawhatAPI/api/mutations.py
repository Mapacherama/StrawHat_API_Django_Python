# mutations.py
from api import db
from api.models import OnePieceCharacter


def create_character_resolver(obj, info, devilfruit, name, crew):
    try:
        print(devilfruit)
        character = OnePieceCharacter(name=name,
                                      crew=crew,
                                      devilfruit=devilfruit)
        db.session.add(character)
        db.session.commit()
        payload = {"success": True, "character": character}
    except ValueError:  # date format errors
        payload = {
            "success":
            False,
            "errors": [
                f"Incorrect date format provided. Date should be in "
                f"the format dd-mm-yyyy"
            ]
        }
    return payload