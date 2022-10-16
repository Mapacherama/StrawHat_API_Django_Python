from ariadne import ObjectType

from . import characters, origin, crew, piratefleet

mutation = ObjectType("Mutation")

#character

mutation.set_field("addCharacter", characters.create_character_resolver)
mutation.set_field("updateCharacter", characters.update_character_resolver)
mutation.set_field("deleteCharacter", characters.delete_character_resolver)

#Origin

mutation.set_field("addOrigin", origin.create_origin_resolver)
mutation.set_field("updateOrigin", origin.update_origin_resolver)
mutation.set_field("deleteOrigin", origin.delete_origin_resolver)

# Crew
mutation.set_field("addCrew", crew.create_crew_resolver)
mutation.set_field("updateCrew", crew.update_crew_resolver)
mutation.set_field("deleteCrew", crew.delete_crew_resolver)

# PirateFleet

mutation.set_field("addPiratefleet", piratefleet.create_piratefleet_resolver)
mutation.set_field("updatePiratefleet", piratefleet.update_piratefleet_resolver)
mutation.set_field("deletePiratefleet", piratefleet.delete_piratefleet_resolver)






