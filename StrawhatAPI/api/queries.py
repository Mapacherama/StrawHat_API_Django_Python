from .models import OnePieceCharacter, Origin
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

# query = Skill.get_query(info=info)
@convert_kwargs_to_snake_case
def listOrigin_resolver(obj, info):
    query = Origin.get_query(info=info)
    query = query.filter(OnePieceCharacter.origin_id == obj.id)
    try:
        origins = [
            origin for origin in Origin.query.all()
        ]

        payload = {"success": True, "origins": origins}
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




