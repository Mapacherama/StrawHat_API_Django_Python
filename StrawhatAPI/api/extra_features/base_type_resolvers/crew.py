from api.models import Crew

def resolve_origin_id(crew_obj: Crew, _info) -> int:
    return origin_obj.id

def resolve_crew_name(crew_obj: Crew, _info) -> str:
    return crew_obj.name

def resolve_crew_oceanoforigin(crew_obj: Crew, _info)-> str:
    return crew_obj.oceanoforigin

def resolve_crew_captain(crew_obj: Crew, _info)-> str:
    return crew_obj.captain

def resolve_crew_mainship(crew_obj: Crew, _info) -> str:
    return crew_obj.mainship

def resolve_crew_totalbounty(crew_obj: Crew, _info)-> int:
    return crew_obj.totalbounty

def resolve_crew_character_id(crew_obj: Crew, _info)-> int:
    return crew_obj.character_id

