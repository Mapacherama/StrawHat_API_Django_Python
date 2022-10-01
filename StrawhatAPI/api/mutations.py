# mutations.py
from api import db
from api.models import OnePieceCharacter
from ariadne import convert_kwargs_to_snake_case


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

@convert_kwargs_to_snake_case
def update_character_resolver(obj, info, id, devilfruit, name, crew):
    try:
        character = OnePieceCharacter.query.get(id)
        if character:
            character.name = name
            character.devilfruit = devilfruit
            character.crew = crew
        db.session.add(character)
        db.session.commit()
        payload = {
            "success": True,
            "character": character.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_character_resolver(obj, info, id):
    try:
        character = OnePieceCharacter.query.get(id)
        db.session.delete(character)
        db.session.commit()
        payload = {"success": True,"character": character.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
