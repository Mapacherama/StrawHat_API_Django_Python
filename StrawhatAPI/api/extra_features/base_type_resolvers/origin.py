from api.models import origin

def resolve_origin_id(origin_obj: origin, _info):
    return origin_obj.id
def resolve_origin_name(origin_obj: origin, _info):
    return origin_obj.name

def resolve_origin_haskingdom(origin_obj: origin, _info)-> bool:
    return origin_obj.hasKingdom







