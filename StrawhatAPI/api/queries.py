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