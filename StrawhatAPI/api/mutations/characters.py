from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

# Character
@convert_kwargs_to_snake_case
def create_character_resolver(obj, info, name, bloodType,
                              occupation, nickName, isAlive,
                              hasDevilFruit, isPartOfFleet,
                              bounty, age, height, birthday
                              ):
    try:
        character = OnePieceCharacter(name = name,
                                      bloodType = bloodType,
                                      occupation = occupation,
                                      nickName = nickName,
                                      isAlive = isAlive,
                                      hasDevilFruit = hasDevilFruit,
                                      isPartOfFleet = isPartOfFleet,
                                      bounty = bounty,
                                      age = age,
                                      height = height,
                                      birthday = birthday
                                      )
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
def update_character_resolver(obj, info, id, name, bloodType,
                              occupation, nickName, isAlive,
                              hasDevilFruit, isPartOfFleet,
                              bounty, age, height, birthday):
    try:
        character = OnePieceCharacter.query.get(id)
        if character:
            name = name,
            bloodType = bloodType,
            occupation = occupation,
            nickName = nickName,
            isAlive = isAlive,
            hasDevilFruit = hasDevilFruit,
            isPartOfFleet = isPartOfFleet,
            bounty = bounty,
            age = age,
            height = height,
            birthday = birthday
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
def delete_character_resolver(obj, info, **kwargs):

    character = OnePieceCharacter.query.get(kwargs["id"])
    db.session.delete(character)
    db.session.commit()

    return create_result()