from api import db
from api.models import OnePieceCharacter, Crew
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case

def create_crew_resolver(obj, info, **kwargs):
    self_status = True
    errors = []
    crew = Crew(**kwargs)
    db.session.add(crew)
    db.session.commit()

    return create_result(status=self_status, errors = errors, crew = crew)

@convert_kwargs_to_snake_case
def update_crew_resolver(obj, info, **kwargs):
    errors = []
    crew = Crew.query.get(kwargs["id"])

    if not product:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])

    crew.update(**kwargs)
    db.session.commit()

    return create_result(status=True, errors = errors, crew = crew)

#Origin

@convert_kwargs_to_snake_case
def delete_crew_resolver(obj, info, **kwargs):
    crew = Crew.query.get(kwargs["id"])
    db.session.delete(crew)
    db.session.commit()

    return create_result()