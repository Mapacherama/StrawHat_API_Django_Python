from api import db
from api.models import crew
from api.extra_features import create_result

from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def listCrews_resolver(obj, info):
    crws = db.session.query(crew).all()    
    return create_result(crew = crws)


@convert_kwargs_to_snake_case
def getSingleCrew_resolver(obj, info, **kwargs):
    crw = db.session.query(crew).get(kwargs["id"])    
    return create_result(crew = crw)