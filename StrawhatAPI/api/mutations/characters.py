from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

# Character
@convert_kwargs_to_snake_case
def create_character_resolver(obj, _info, **kwargs):

    character = OnePieceCharacter(**kwargs)
    db.session.add(character)
    db.session.commit()

    return create_result(character)


def update_character_resolver(obj, _info, **kwargs):
    errors = []
    character = OnePieceCharacter.query.get(kwargs["id"])
    print(character.isalive)
    print(kwargs)
    if not character:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])
    #Look at the variable names of the dictionary ea in the kwargs dictionary.
    if kwargs.get("hasdevil_fruit"):
        character.hasdevilFruit = kwargs["hasdevil_fruit"]

    if kwargs.get("ispart_offleet"):
        character.ispartOffleet= kwargs["ispart_offleet"]

    if kwargs.get("is_alive"):
        character.isalive = kwargs["is_alive"]

    character.update(**kwargs)
    db.session.commit()

    return create_result(errors= errors, character = character)

@convert_kwargs_to_snake_case
def delete_character_resolver(obj, info, **kwargs):

    character = OnePieceCharacter.query.get(kwargs["id"])
    db.session.delete(character)
    db.session.commit()

    return create_result(character)