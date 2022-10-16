from api import db
from api.models import OnePieceCharacter, origin
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_origin_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    Origin = origin(**kwargs)
    db.session.add(Origin)
    db.session.commit()

    return create_result(status=self_status, errors = errors, origin = Origin)

@convert_kwargs_to_snake_case
def update_origin_resolver(obj, info, **kwargs):
    errors = []
    orign = db.session.query(origin).get(kwargs["id"])

    print(kwargs)

    if not orign:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])

    if kwargs.get("has_kingdom"):
        print(kwargs["has_kingdom"])
        orign.hasKingdom = kwargs["has_kingdom"]

    orign.update(**kwargs)
    db.session.commit()

    return create_result(errors= errors, origin = orign)

#Origin

@convert_kwargs_to_snake_case
def delete_origin_resolver(obj, info, **kwargs):
    orign = origin.query.get(kwargs["id"])
    db.session.delete(orign)
    db.session.commit()

    return create_result()