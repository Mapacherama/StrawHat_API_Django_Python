from api.models import OnePieceCharacter
def resolve_character_id(character_obj: OnePieceCharacter, _info) -> int:
    return character_obj.id

def resolve_character_name(character_obj: OnePieceCharacter, _info) -> int:
    return character_obj.name

def resolve_character_bloodtype(character_obj: OnePieceCharacter, _info) -> str:
    return character_obj.bloodtype

def resolve_character_occupation(character_obj: OnePieceCharacter, _info) -> str:
    return character_obj.occupation

def resolve_character_nickname(character_obj: OnePieceCharacter, _info) -> str:
    return character_obj.nickname

def resolve_character_isalive(character_obj: OnePieceCharacter, _info) -> bool:
    return character_obj.isalive

def resolve_character_hasdevilFruit(character_obj: OnePieceCharacter, _info) -> bool:
    return character_obj.hasdevilFruit

def resolve_character_ispartOffleet(character_obj: OnePieceCharacter, _info) -> bool:
    return character_obj.ispartOffleet
def resolve_character_bounty(character_obj: OnePieceCharacter, _info) -> int:
    return character_obj.bounty
def resolve_character_age(character_obj: OnePieceCharacter, _info) -> int:
    return character_obj.age

def resolve_character_height(character_obj: OnePieceCharacter, _info) -> int:
    return character_obj.height

def resolve_character_birthday(character_obj: OnePieceCharacter, _info):
    return character_obj.birthday



