from api import db
from api.extra_features import create_result
from api.models import OnePieceCharacter

from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listOnePieceCharacters_resolver(obj, info):
           
    characters = db.session.query(OnePieceCharacter).all()
    
    return create_result(characters = characters)


@convert_kwargs_to_snake_case
def getSingleCharacter_resolver(obj, info, **kwargs):    
        character = OnePieceCharacter.query.get(kwargs["id"])

        
        return create_result(character = character)
