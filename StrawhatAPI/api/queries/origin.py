from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features import create_result


from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listOrigin_resolver(obj, info):

    orgns = db.session.query(origin).all()
        
    return create_result(origin = orgns)


@convert_kwargs_to_snake_case
def getSingleOrigin_resolver(obj, info, **kwargs):

    orgn = db.session.query(origin).get(kwargs["id"])

    return create_result(origin = orgn)
