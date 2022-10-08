from api import db
from api.models import OnePieceCharacter
from api.extra_features import create_result

from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listOrigin_resolver(obj, info):

    origin = db.session.query(Origin).all()
        
    return create_result(origin = origin)


@convert_kwargs_to_snake_case
def getSingleOrigin_resolver(obj, info, id):
    try:
        origin = Origin.query.filter(OnePieceCharacter.origin_id == id).first()
        payload = {"success": True, "origin": origin}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Character item matching {id} not found"]
        }
    return payload
