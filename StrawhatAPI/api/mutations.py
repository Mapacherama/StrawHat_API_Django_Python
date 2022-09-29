from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import OnePieceCharacter


@convert_kwargs_to_snake_case
def create_character_resolver(obj, name, crew, devilFruit):
    try:
        character = OnePieceCharacter(name=name,
                                      crew=crew,
                                      devilFruit=devilFruit)
        db.session.add(character)
        db.session.commit()

        payload = {"success": True, "post": character.to_dict()}
    except ValueError:  # date format errors
        payload = {"success": False, "errors": [f"Incorrect input provided"]}
    return payload