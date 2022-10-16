from api.models import piratefleet

def resolve_piratefleet_id(piratefleet_obj: piratefleet, _info):
    return piratefleet_obj.id

def resolve_piratefleet_name(piratefleet_obj: piratefleet, _info) -> str:
    return piratefleet_obj.name

def resolve_piratefleet_captain(piratefleet_obj: piratefleet, _info)-> str:
    return piratefleet_obj.captain

def resolve_piratefleet_totalpeople(piratefleet_obj: piratefleet, _info)-> int:
    return piratefleet_obj.totalpeople

def resolve_piratefleet_totalbounty(piratefleet_obj: piratefleet, _info)-> int:
    return piratefleet_obj.totalbounty

def resolve_piratefleet_character_id(piratefleet_obj: piratefleet, _info)-> int:
    return piratefleet_obj.character_id