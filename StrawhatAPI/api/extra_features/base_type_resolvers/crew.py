from api.models import Crew

def resolve_origin_id(crew_obj: Crew, _info) -> int:
    return origin_obj.id

def resolve_origin_name(crew_obj: Crew, _info) -> str:
    return crew_obj.name

def resolve_origin_haskingdom(crew_obj: Crew, _info)-> str:
    return crew_obj.oceanoforigin

def resolve_origin_character_id(crew_obj: Crew, _info)-> str:
    return crew_obj.captain

def resolve_origin_name(crew_obj: Crew, _info) -> str:
    return crew_obj.mainship

def resolve_origin_haskingdom(crew_obj: Crew, _info)-> int:
    return crew_obj.totalbounty

def resolve_origin_character_id(crew_obj: Crew, _info)-> int:
    return crew_obj.character_id

