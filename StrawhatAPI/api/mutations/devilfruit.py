from api import db
from api.models import devilfruit
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_devilfruit_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    Devilfruit = devilfruit(**kwargs)
    db.session.add(Devilfruit)
    db.session.commit()

    return create_result(status=self_status, errors = errors, origin = Origin)

@convert_kwargs_to_snake_case
def update_devilfruit_resolver(obj, info, **kwargs):
    errors = []
    Devilfruit = db.session.query(devilfruit).get(kwargs["id"])

    if not orign:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])

    Devilfruit.update(**kwargs)
    db.session.commit()

    return create_result(errors= errors, devilfruit = Devilfruit)

#Origin

@convert_kwargs_to_snake_case
def delete_devilfruit_resolver(obj, info, **kwargs):
    Devilfruit = devilfruit.query.get(kwargs["id"])
    db.session.delete(Devilfruit)
    db.session.commit()

    return create_result()