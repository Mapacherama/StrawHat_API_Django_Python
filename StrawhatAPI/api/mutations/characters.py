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

@convert_kwargs_to_snake_case
def update_character_resolver(obj, _info, **kwargs):

    character = OnePieceCharacter.query.get(kwargs["id"])
    if not character:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])
    db.session.update(**kwargs)
    db.session.commit()

    return create_result(character = character)

@convert_kwargs_to_snake_case
def delete_character_resolver(obj, info, **kwargs):

    character = OnePieceCharacter.query.get(kwargs["id"])
    db.session.delete(character)
    db.session.commit()

    return create_result()