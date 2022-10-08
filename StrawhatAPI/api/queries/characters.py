from api import db
from api.extra_features import create_result
from api.models import OnePieceCharacter, Origin

from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listOnePieceCharacters_resolver(obj, info):
           
    characters = OnePieceCharacter.query.all()       
    
    return create_result(characters = characters)


@convert_kwargs_to_snake_case
def getSingleCharacter_resolver(obj, info, id):
    try:
        character = OnePieceCharacter.query.get(id)
        
    except KeyError: 
        pass
        
        return create_result(character = character)
