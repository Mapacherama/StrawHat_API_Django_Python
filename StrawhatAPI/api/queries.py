from .models import OnePieceCharacter
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listOnePieceCharacters_resolver(obj, info):
    try:
        onePieceCharacters = [
            character for character in OnePieceCharacter.query.all()
        ]
        print(onePieceCharacters)
        payload = {"success": True, "onepiececharacters": onePieceCharacters}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getSingleCharacter_resolver(obj, info, id):
    try:
        character = OnePieceCharacter.query.get(id)
        payload = {"success": True, "character": character}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Character item matching {id} not found"]
        }
    return payload
@convert_kwargs_to_snake_case
def listResidence_resolver(obj, info):
    try:
        onePieceCharacters = [
            residence for residence in Residence.query.all()
        ]
        print(onePieceCharacters)
        payload = {"success": True, "recidences": onePieceCharacters}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getSingleResidence_resolver(obj, info, id):
    try:
        recidence = Residence.query.get(id)
        payload = {"success": True, "recidence": character}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Character item matching {id} not found"]
        }
    return payload




