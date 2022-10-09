from ariadne import ObjectType

from . import character, origin

character_type = ObjectType("character")

character_type.set_field("id", character.resolve_character_id)
character_type.set_field("name", character.resolve_character_name)
character_type.set_field("bloodType", character.resolve_character_bloodtype)
character_type.set_field("occupation",  character.resolve_character_occupation)
character_type.set_field("nickName",  character.resolve_character_nickname)
character_type.set_field("isAlive",  character.resolve_character_isalive)
character_type.set_field("hasDevilFruit",  character.resolve_character_hasdevilFruit)
character_type.set_field("isPartOfFleet",  character.resolve_character_ispartOffleet)
character_type.set_field("bounty",  character.resolve_character_bounty)
character_type.set_field("age",  character.resolve_character_age)
character_type.set_field("height",  character.resolve_character_height)
character_type.set_field("birthday",  character.resolve_character_birthday)

origin_type = ObjectType("origin")

origin_type.set_field("id", origin.resolve_origin_id)
origin_type.set_field("name", origin.resolve_origin_name)
origin_type.set_field("hasKingdom", origin.resolve_origin_haskingdom)


