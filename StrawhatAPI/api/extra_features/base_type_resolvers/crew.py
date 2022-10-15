from api.models import crew

def resolve_crew_id(crew_obj: crew, _info):
    return crew_obj.id

def resolve_crew_name(crew_obj: crew, _info) -> str:
    return crew_obj.name

def resolve_crew_oceanOfOrigin(crew_obj: crew, _info) -> str:
    return crew_obj.oceanoforigin

def resolve_crew_captain(crew_obj: crew, _info) -> str:
    return crew_obj.captain

def resolve_crew_mainship(crew_obj: crew, _info) -> str:
    return crew_obj.mainship

def resolve_crew_totalbounty(crew_obj: crew, _info) -> int:
    return crew_obj.totalbounty

def resolve_crew_character_id(crew_obj: crew, _info)-> int:
    return crew_obj.character_id

