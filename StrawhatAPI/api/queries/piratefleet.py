from api import db
from api.models import piratefleet
from api.extra_features import create_result

from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def listPiratefleets_resolver(obj, info):
    Piratefleet = db.session.query(piratefleet).all()

    return create_result(piratefleet=Piratefleet)


@convert_kwargs_to_snake_case
def getSinglePiratefleet_resolver(obj, info, **kwargs):
    Piratefleet = db.session.query(piratefleet).get(kwargs["id"])

    return create_result(piratefleet=Piratefleet)
