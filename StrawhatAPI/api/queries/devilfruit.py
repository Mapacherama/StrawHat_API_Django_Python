from api import db
from api.models import devilfruit
from api.extra_features import create_result

from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listDevilfruits_resolver(obj, info):
    Devilfruit = db.session.query(devilfruit).all()
    return create_result(devilfruit = Devilfruit)


@convert_kwargs_to_snake_case
def getSingleDevilfruit_resolver(obj, info, **kwargs):
    Devilfruit = db.session.query(devilfruit).get(kwargs["id"])
    return create_result(devilfruit = Devilfruit)