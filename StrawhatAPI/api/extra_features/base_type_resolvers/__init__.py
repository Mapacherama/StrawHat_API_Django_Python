from ariadne import ObjectType

from . import character, origin, crew, piratefleet, devilfruit

character_type = ObjectType("characterType")

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
character_type.set_field("image",  character.resolve_character_image)
character_type.set_field("origin",  character.resolve_character_origin)
character_type.set_field("crew",  character.resolve_character_crew)
character_type.set_field("piratefleet",  character.resolve_character_piratefleet)
character_type.set_field("devilfruit",  character.resolve_character_devilfruit)


origin_type = ObjectType("originType")

origin_type.set_field("id", origin.resolve_origin_id)
origin_type.set_field("name", origin.resolve_origin_name)
origin_type.set_field("hasKingdom", origin.resolve_origin_haskingdom)
origin_type.set_field("character_id", origin.resolve_origin_character_id)

crew_type = ObjectType("crewType")

crew_type.set_field("id", crew.resolve_crew_id)
crew_type.set_field("name", crew.resolve_crew_name)
crew_type.set_field("oceanoforigin", crew.resolve_crew_oceanOfOrigin)
crew_type.set_field("captain", crew.resolve_crew_captain)
crew_type.set_field("mainship", crew.resolve_crew_mainship)
crew_type.set_field("totalbounty", crew.resolve_crew_totalbounty)
crew_type.set_field("character_id", crew.resolve_crew_character_id)

piratefleet_type = ObjectType("piratefleetType")

piratefleet_type.set_field("id", piratefleet.resolve_piratefleet_id)
piratefleet_type.set_field("name", piratefleet.resolve_piratefleet_name)
piratefleet_type.set_field("captain", piratefleet.resolve_piratefleet_captain)
piratefleet_type.set_field("totalpeople", piratefleet.resolve_piratefleet_totalpeople)
piratefleet_type.set_field("totalbounty", piratefleet.resolve_piratefleet_totalbounty)
piratefleet_type.set_field("character_id", piratefleet.resolve_piratefleet_character_id)

devilfruit_type = ObjectType("devilfruitType")

devilfruit_type.set_field("id", devilfruit.resolve_devilfruit_id)
devilfruit_type.set_field("name", devilfruit.resolve_devilfruit_name)
devilfruit_type.set_field("meaning", devilfruit.resolve_devilfruit_haskingdom)
devilfruit_type.set_field("type", devilfruit.resolve_devilfruit_haskingdom)
devilfruit_type.set_field("character_id", devilfruit.resolve_devilfruit_character_id)



