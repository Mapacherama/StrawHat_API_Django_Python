from api import db
from api.models import piratefleet
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_piratefleet_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    Piratefleet = piratefleet(**kwargs)
    db.session.add(piratefleet)
    db.session.commit()

    return create_result(status=self_status, errors = errors, piratefleet = Piratefleet)

@convert_kwargs_to_snake_case
def update_piratefleet_resolver(obj, info, **kwargs):
    errors = []
    Piratefleet = db.session.query(piratefleet).get(kwargs["id"])

    if not orign:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])

    Piratefleet.update(**kwargs)
    db.session.commit()

    return create_result(errors= errors, piratefleet = Piratefleet)

#Piratefleet

@convert_kwargs_to_snake_case
def delete_piratefleet_resolver(obj, info, **kwargs):
    Piratefleet = piratefleet.query.get(kwargs["id"])
    db.session.delete(Piratefleet)
    db.session.commit()

    return create_result()