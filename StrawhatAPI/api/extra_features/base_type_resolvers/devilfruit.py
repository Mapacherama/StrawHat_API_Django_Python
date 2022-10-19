from api.models import devilfruit, devilfruittype

def resolve_devilfruit_id(devilfruit_obj: devilfruit, _info):
    return devilfruit_obj.id

def resolve_devilfruit_name(devilfruit_obj: devilfruit, _info) -> str:
    return devilfruit_obj.name

def resolve_devilfruit_meaning(devilfruit_obj: devilfruit, _info) -> str:
    return devilfruit_obj.meaning

def resolve_devilfruit_typeof(devilfruit_obj: devilfruit, _info) -> str:
    return devilfruit_obj.typeofdevilfruit.value

def resolve_devilfruit_character_id(devilfruit_obj: devilfruit, _info)-> int:
    return devilfruit_obj.character_id
