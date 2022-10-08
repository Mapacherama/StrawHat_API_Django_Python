from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_origin_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    Origin = origin(kwargs)
    db.session.add(origin)

    return create_result(status=self_status, errors = errors, origin = Origin)

@convert_kwargs_to_snake_case
def update_origin_resolver(obj, info, id, **kwargs):
    errors = []
    origin = origin.query.get(kwargs["id"])
    if not product:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])

        product.update(**kwargs)
        db.session.commit()


    return create_result(errors=errors, origin = origin)



#Origin

@convert_kwargs_to_snake_case
def delete_origin_resolver(obj, info, **kwargs):
    origin = origin.query.get(kwargs["id"])
    db.session.delete(origin)
    db.session.commit()

    return create_result(status=True, errors= [], origin = origin)