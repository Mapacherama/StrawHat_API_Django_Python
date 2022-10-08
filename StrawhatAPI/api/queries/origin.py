from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features import create_result

from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listOrigin_resolver(obj, info):

    origin = db.session.query(origin).all()
        
    return create_result(origin = origin)


@convert_kwargs_to_snake_case
def getSingleOrigin_resolver(obj, info, id):
    origin = db.session.query(origin).filter(OnePieceCharacter.origin_id == id).first()

    return origin
