from api import db
from api.models import OnePieceCharacter, Origin
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_origin_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    origin = Origin(**kwargs)
    db.session.add(origin)

    return create_result(status=self_status, errors= errors, origin = origin)

@convert_kwargs_to_snake_case
def update_origin_resolver(obj, info, id, name, haskingdom):
    try:
        origin = Origin.query.get(id)
        if origin:
            origin.name = name
            origin.haskingdom = haskingdom            
        db.session.add(origin)
        db.session.commit()
        payload = {
            "success": True,
            "character": origin.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload



#Origin

@convert_kwargs_to_snake_case
def delete_origin_resolver(obj, info, id):
    try:
        origin = Origin.query.get(id)
        db.session.delete(origin)
        db.session.commit()
        payload = {"success": True,"character": origin.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return