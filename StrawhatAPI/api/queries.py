from .models import OnePieceCharacter


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


def getSingleCharacter_resolver(obj, info, id):
    try:
        character = OnePieceCharacter.query.get(id)
        print(character)
        payload = {"success": True, "character": character}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Character item matching {id} not found"]
        }
    return payload
